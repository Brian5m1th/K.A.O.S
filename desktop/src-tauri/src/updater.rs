use serde::{Deserialize, Serialize};
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
    
    // Localizar o arquivo docker-compose.yml
    let mut compose_path = std::path::PathBuf::new();
    let mut found = false;
    
    let env_workspace = std::env::var("KAOS_WORKSPACE").ok().map(std::path::PathBuf::from);
    let current_dir = std::env::current_dir().unwrap_or_default();
    let exe_dir = std::env::current_exe().unwrap_or_default().parent().unwrap_or(std::path::Path::new("")).to_path_buf();
    let hardcoded_workspace = std::path::PathBuf::from("C:\\workspace\\Freelancer\\K.A.O.S");

    let mut search_dirs = vec![];
    if let Some(p) = env_workspace { search_dirs.push(p); }
    search_dirs.push(current_dir);
    search_dirs.push(exe_dir);
    search_dirs.push(hardcoded_workspace);

    for dir in search_dirs {
        let mut current = dir.clone();
        for _ in 0..5 {
            let path = current.join("infra/docker/docker-compose.yml");
            if path.exists() {
                compose_path = path;
                found = true;
                break;
            }
            if let Some(parent) = current.parent() {
                current = parent.to_path_buf();
            } else {
                break;
            }
        }
        if found { break; }
    }
    
    if !found {
        return Err("Nao foi possivel encontrar o arquivo infra/docker/docker-compose.yml. Defina a variavel de ambiente KAOS_WORKSPACE apontando para a raiz do projeto.".to_string());
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

// ── Fase 6: Bootstrap Commands ─────────────────────────────────────────────

#[derive(Serialize)]
pub struct DockerVersion {
    pub available: bool,
    pub version: Option<String>,
}

#[derive(Serialize)]
pub struct DockerEngine {
    pub running: bool,
    pub info: Option<String>,
}

#[derive(Serialize)]
pub struct BackendHealth {
    pub reachable: bool,
    pub status: Option<String>,
    pub error: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct BootstrapState {
    pub state: String,
    pub is_ready: bool,
    pub degraded: bool,
    pub boot_complete: bool,
    pub stages: Vec<serde_json::Value>,
    pub errors: Vec<String>,
    pub total_elapsed_ms: f64,
}

/// Comando 1: Verificar se o CLI do Docker esta instalado.
#[tauri::command]
pub async fn check_docker() -> DockerVersion {
    println!("[docker] Verificando instalacao do Docker CLI...");
    let output = std::process::Command::new("docker")
        .arg("--version")
        .output();

    match output {
        Ok(out) if out.status.success() => {
            let version = String::from_utf8_lossy(&out.stdout).trim().to_string();
            println!("[docker] Docker encontrado: {}", version);
            DockerVersion {
                available: true,
                version: Some(version),
            }
        }
        Ok(out) => {
            let stderr = String::from_utf8_lossy(&out.stderr);
            println!("[docker] Docker CLI nao disponivel: {}", stderr);
            DockerVersion {
                available: false,
                version: None,
            }
        }
        Err(e) => {
            println!("[docker] Erro ao executar docker --version: {}", e);
            DockerVersion {
                available: false,
                version: None,
            }
        }
    }
}

/// Comando 2: Verificar se o Docker Engine esta rodando.
#[tauri::command]
pub async fn check_docker_engine() -> DockerEngine {
    println!("[docker] Verificando Docker Engine...");
    let output = std::process::Command::new("docker")
        .args(["info", "--format", "{{.ServerVersion}}"])
        .output();

    match output {
        Ok(out) if out.status.success() => {
            let version = String::from_utf8_lossy(&out.stdout).trim().to_string();
            println!("[docker] Docker Engine rodando (versao: {})", version);
            DockerEngine {
                running: true,
                info: Some(version),
            }
        }
        Ok(out) => {
            let stderr = String::from_utf8_lossy(&out.stderr).trim().to_string();
            println!("[docker] Docker Engine nao respondeu: {}", stderr);
            DockerEngine {
                running: false,
                info: Some(stderr),
            }
        }
        Err(e) => {
            println!("[docker] Erro ao verificar docker info: {}", e);
            DockerEngine {
                running: false,
                info: None,
            }
        }
    }
}

/// Comando 3: Verificar saude do backend K.A.O.S.
#[tauri::command]
pub async fn check_backend_health(server_url: Option<String>) -> BackendHealth {
    let base = server_url.unwrap_or_else(|| "http://localhost:8000".to_string());
    let url = format!("{}/health", base.trim_end_matches('/'));
    println!("[backend] Verificando saude do backend em {}...", url);

    match reqwest::get(&url).await {
        Ok(resp) => {
            let status = resp.status().to_string();
            let body: serde_json::Value = resp.json().await.unwrap_or_default();
            let status_msg = body.get("status").and_then(|s| s.as_str()).unwrap_or(&status).to_string();
            println!("[backend] Backend respondeu: {}", status_msg);
            BackendHealth {
                reachable: true,
                status: Some(status_msg),
                error: None,
            }
        }
        Err(e) => {
            println!("[backend] Backend inacessivel: {}", e);
            BackendHealth {
                reachable: false,
                status: None,
                error: Some(e.to_string()),
            }
        }
    }
}

/// Comando 4: Obter estado do bootstrap do backend.
#[tauri::command]
pub async fn get_bootstrap_state(server_url: Option<String>) -> BootstrapState {
    let base = server_url.unwrap_or_else(|| "http://localhost:8000".to_string());
    let url = format!("{}/api/system/bootstrap", base.trim_end_matches('/'));
    println!("[bootstrap] Obtendo estado do bootstrap de {}...", url);

    match reqwest::get(&url).await {
        Ok(resp) if resp.status().is_success() => {
            let data: serde_json::Value = resp.json().await.unwrap_or_default();
            let state = data.get("state").and_then(|s| s.as_str()).unwrap_or("unknown").to_string();
            let is_ready = data.get("is_ready").and_then(|v| v.as_bool()).unwrap_or(false);
            let degraded = data.get("degraded").and_then(|v| v.as_bool()).unwrap_or(false);
            let boot_complete = data.get("boot_complete").and_then(|v| v.as_bool()).unwrap_or(false);
            let stages = data.get("stages").and_then(|v| v.as_array()).cloned().unwrap_or_default();
            let errors = data.get("errors").and_then(|v| v.as_array())
                .map(|arr| arr.iter().filter_map(|v| v.as_str().map(|s| s.to_string())).collect())
                .unwrap_or_default();
            let total_elapsed_ms = data.get("total_elapsed_ms").and_then(|v| v.as_f64()).unwrap_or(0.0);

            println!("[bootstrap] Estado: {} ready={} degraded={}", state, is_ready, degraded);
            BootstrapState {
                state,
                is_ready,
                degraded,
                boot_complete,
                stages,
                errors,
                total_elapsed_ms,
            }
        }
        Ok(resp) => {
            println!("[bootstrap] Backend retornou status {}", resp.status());
            BootstrapState {
                state: "backend_error".to_string(),
                is_ready: false,
                degraded: false,
                boot_complete: false,
                stages: vec![],
                errors: vec![format!("Backend retornou HTTP {}", resp.status())],
                total_elapsed_ms: 0.0,
            }
        }
        Err(e) => {
            println!("[bootstrap] Backend inacessivel: {}", e);
            BootstrapState {
                state: "backend_unreachable".to_string(),
                is_ready: false,
                degraded: false,
                boot_complete: false,
                stages: vec![],
                errors: vec![format!("Backend inacessivel: {}", e)],
                total_elapsed_ms: 0.0,
            }
        }
    }
}
