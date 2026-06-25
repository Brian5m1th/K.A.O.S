use serde::Serialize;
use std::sync::Mutex;
use tauri::{AppHandle, Emitter, Manager};
use tauri_plugin_updater::UpdaterExt;

#[derive(Serialize)]
pub struct UpdateResult {
    pub available: bool,
    pub version: Option<String>,
    pub date: Option<String>,
    pub body: Option<String>,
}

#[derive(Serialize, Clone)]
struct ProgressPayload {
    downloaded: u64,
    total: Option<u64>,
}

/// Cache do Update e bytes baixados entre download_and_install e install_update (G-11)
pub struct UpdaterState {
    pub pending_update: Mutex<Option<(tauri_plugin_updater::Update, Vec<u8>)>>,
}

#[tauri::command]
pub fn get_app_version(app: AppHandle) -> String {
    let ver = app.package_info().version.to_string();
    println!("[updater] Versao do aplicativo solicitada pelo frontend: {}", ver);
    ver
}

#[tauri::command]
pub async fn check_for_update(app: AppHandle) -> Result<UpdateResult, String> {
    println!("[updater] Verificando se ha atualizacoes...");
    let updater = app.updater().map_err(|e| e.to_string())?;
    let update = match updater.check().await {
        Ok(u) => u,
        Err(e) => {
            let err_str = e.to_string();
            println!("[updater] Erro ao verificar atualizacao: {}", err_str);
            if err_str.contains("relative URL without a base") || err_str.contains("empty") {
                return Ok(UpdateResult {
                    available: false,
                    version: None,
                    date: None,
                    body: None,
                });
            }
            return Err(err_str);
        }
    };

    if let Some(update) = update {
        println!("[updater] Atualizacao disponivel! Versao: {}", update.version);
        Ok(UpdateResult {
            available: true,
            version: Some(update.version.clone()),
            date: update.date.map(|d| d.to_string()),
            body: update.body.clone(),
        })
    } else {
        println!("[updater] Nenhuma atualizacao disponivel.");
        Ok(UpdateResult {
            available: false,
            version: None,
            date: None,
            body: None,
        })
    }
}

#[tauri::command]
pub async fn download_and_install(app: AppHandle) -> Result<(), String> {
    println!("[updater] Iniciando download da atualizacao...");
    let updater = app.updater().map_err(|e| e.to_string())?;
    let update = updater.check().await.map_err(|e| e.to_string())?;

    let update = match update {
        Some(u) => u,
        None => {
            println!("[updater] Download cancelado: Nenhuma atualizacao disponivel.");
            return Err("Nenhuma atualizacao disponivel".into());
        }
    };

    // G-12: clonar AppHandle antes do callback (thread de background)
    let app_for_progress = app.clone();
    let mut downloaded = 0;
    
    let bytes = update
        .download(
            move |chunk_length, content_length| {
                downloaded += chunk_length as u64;
                let _ = app_for_progress.emit(
                    "update:progress",
                    ProgressPayload {
                        downloaded,
                        total: content_length,
                    },
                );
            },
            || {},
        )
        .await
        .map_err(|e| {
            println!("[updater] Download falhou: {}", e);
            let _ = app.emit(
                "update:error",
                serde_json::json!({ "message": e.to_string() }),
            );
            format!("Download falhou: {}", e)
        })?;

    println!("[updater] Download concluido com sucesso. Salvando estado pendente.");
    // G-11: cachear update e bytes para install_update
    let state = app.state::<UpdaterState>();
    *state.pending_update.lock().unwrap() = Some((update, bytes));

    let _ = app.emit("update:ready", ());
    Ok(())
}

#[tauri::command]
pub async fn install_update(app: AppHandle) -> Result<(), String> {
    println!("[updater] Iniciando instalacao da atualizacao...");
    let state = app.state::<UpdaterState>();
    let pending = state.pending_update.lock().unwrap().take();

    match pending {
        Some((update, bytes)) => {
            println!("[updater] Aplicando atualizacao...");
            update
                .install(bytes)
                .map_err(|e| {
                    println!("[updater] Instalacao falhou: {}", e);
                    format!("Install falhou: {}", e)
                })?;
            println!("[updater] Instalacao bem-sucedida. Reiniciando o aplicativo...");
            #[allow(unreachable_code)]
            {
                app.restart();
                Ok(())
            }
        }
        None => {
            println!("[updater] Instalacao cancelada: Nenhum update baixado.");
            Err("Nenhum update baixado. Execute download_and_install primeiro.".into())
        }
    }
}

#[tauri::command]
pub async fn ensure_docker_services() -> Result<(), String> {
    println!("[docker] Verificando se os servicos do Docker estao ativos...");
    
    // Localizar o arquivo docker-compose.yml subindo a arvore de diretorios a partir da pasta atual
    let mut compose_path = match std::env::current_dir() {
        Ok(dir) => dir,
        Err(e) => return Err(format!("Erro ao obter diretorio atual: {}", e)),
    };
    
    let mut found = false;
    for _ in 0..5 {
        let path = compose_path.join("infra/docker/docker-compose.yml");
        if path.exists() {
            compose_path = path;
            found = true;
            break;
        }
        if let Some(parent) = compose_path.parent() {
            compose_path = parent.to_path_buf();
        } else {
            break;
        }
    }
    
    if !found {
        // Fallback: tentar no diretorio padrão relativo ao workspace local
        compose_path = std::path::PathBuf::from("../../infra/docker/docker-compose.yml");
    }

    println!("[docker] Caminho do docker-compose: {:?}", compose_path);

    let mut cmd = std::process::Command::new("docker");
    cmd.args(["compose", "-f", compose_path.to_string_lossy().as_ref(), "up", "-d"]);

    #[cfg(windows)]
    {
        // 0x08000000 = CREATE_NO_WINDOW
        std::os::windows::process::CommandExt::creation_flags(&mut cmd, 0x08000000);
    }

    let output = cmd.output();

    match output {
        Ok(out) => {
            let stderr = String::from_utf8_lossy(&out.stderr);
            if out.status.success() {
                println!("[docker] Servicos do Docker iniciados com sucesso!");
                Ok(())
            } else {
                println!("[docker] Falha ao iniciar servicos do Docker: {}", stderr);
                Err(format!("Docker compose falhou: {}", stderr))
            }
        }
        Err(e) => {
            println!("[docker] Erro ao executar comando docker: {}", e);
            Err(format!("Nao foi possivel executar o comando docker. Certifique-se de que o Docker Desktop esta instalado e rodando. Erro: {}", e))
        }
    }
}
