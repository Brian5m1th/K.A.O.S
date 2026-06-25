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
pub async fn check_for_update(app: AppHandle) -> Result<UpdateResult, String> {
    let updater = app.updater().map_err(|e| e.to_string())?;
    let update = match updater.check().await {
        Ok(u) => u,
        Err(e) => {
            let err_str = e.to_string();
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
        Ok(UpdateResult {
            available: true,
            version: Some(update.version.clone()),
            date: update.date.map(|d| d.to_string()),
            body: update.body.clone(),
        })
    } else {
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
    let updater = app.updater().map_err(|e| e.to_string())?;
    let update = updater.check().await.map_err(|e| e.to_string())?;

    let update = match update {
        Some(u) => u,
        None => return Err("Nenhuma atualizacao disponivel".into()),
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
            let _ = app.emit(
                "update:error",
                serde_json::json!({ "message": e.to_string() }),
            );
            format!("Download falhou: {}", e)
        })?;

    // G-11: cachear update e bytes para install_update
    let state = app.state::<UpdaterState>();
    *state.pending_update.lock().unwrap() = Some((update, bytes));

    let _ = app.emit("update:ready", ());
    Ok(())
}

#[tauri::command]
pub async fn install_update(app: AppHandle) -> Result<(), String> {
    let state = app.state::<UpdaterState>();
    let pending = state.pending_update.lock().unwrap().take();

    match pending {
        Some((update, bytes)) => update
            .install(bytes)
            .map_err(|e| format!("Install falhou: {}", e)),
        None => Err("Nenhum update baixado. Execute download_and_install primeiro.".into()),
    }
}
