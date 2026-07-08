mod updater;

use serde::{Deserialize, Serialize};
use updater::UpdaterState;

#[derive(Debug, Serialize, Deserialize)]
pub struct HealthResponse {
    pub status: String,
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .manage(UpdaterState {
            pending_update: std::sync::Mutex::new(None),
        })
        .plugin(tauri_plugin_store::Builder::new().build())
        .plugin(tauri_plugin_updater::Builder::new().build())
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![
            updater::get_app_version,
            updater::check_for_update,
            updater::download_and_install,
            updater::install_update,
            updater::ensure_docker_services,
            // Fase 6: Bootstrap
            updater::check_docker,
            updater::check_docker_engine,
            updater::check_backend_health,
            updater::get_bootstrap_state,
        ])
        .run(tauri::generate_context!())
        .expect("error while running KAOS");
}
