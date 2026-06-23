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

/// Cache do Update entre download_and_install e install_update (G-11)
pub struct UpdaterState {
    pub pending_update: Mutex<Option<tauri_plugin_updater::Update>>,
}

#[tauri::command]
pub async fn check_for_update(app: AppHandle) -> Result<UpdateResult, String> {
    let updater = app.updater().map_err(|e| e.to_string())?;
    let update = updater.check().await.map_err(|e| e.to_string())?;

    Ok(UpdateResult {
        available: update.is_available(),
        version: update.version().map(|v| v.to_string()),
        date: update.date().map(|d| d.to_string()),
        body: update.body().map(|b| b.to_string()),
    })
}

#[tauri::command]
pub async fn download_and_install(app: AppHandle) -> Result<(), String> {
    let updater = app.updater().map_err(|e| e.to_string())?;
    let update = updater.check().await.map_err(|e| e.to_string())?;

    if !update.is_available() {
        return Err("Nenhuma atualizacao disponivel".into());
    }

    // G-12: clonar AppHandle antes do callback (thread de background)
    let app_for_progress = app.clone();
    update
        .download(
            move |chunk, content_length| {
                let _ = app_for_progress.emit(
                    "update:progress",
                    ProgressPayload {
                        downloaded: chunk.position + chunk.data.len() as u64,
                        total: Some(content_length),
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

    // G-11: cachear para install_update
    let state = app.state::<UpdaterState>();
    *state.pending_update.lock().unwrap() = Some(update);

    let _ = app.emit("update:ready", ());
    Ok(())
}

#[tauri::command]
pub async fn install_update(app: AppHandle) -> Result<(), String> {
    let state = app.state::<UpdaterState>();
    let update = state.pending_update.lock().unwrap().take();

    match update {
        Some(update) => update
            .install()
            .map_err(|e| format!("Install falhou: {}", e)),
        None => Err("Nenhum update baixado. Execute download_and_install primeiro.".into()),
    }
}
