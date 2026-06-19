use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct HealthResponse {
    pub status: String,
}

#[tauri::command]
async fn check_server(url: String) -> Result<HealthResponse, String> {
    let client = reqwest::Client::builder()
        .timeout(std::time::Duration::from_secs(5))
        .build()
        .map_err(|e| e.to_string())?;

    let resp = client
        .get(&format!("{}/health", url.trim_end_matches('/')))
        .send()
        .await
        .map_err(|e| format!("Connection failed: {}", e))?;

    let health: HealthResponse = resp
        .json()
        .await
        .map_err(|e| format!("Invalid response: {}", e))?;

    Ok(health)
}

#[tauri::command]
async fn check_ollama(url: String) -> Result<String, String> {
    let client = reqwest::Client::builder()
        .timeout(std::time::Duration::from_secs(5))
        .build()
        .map_err(|e| e.to_string())?;

    let resp = client
        .get(&format!("{}/api/tags", url.trim_end_matches('/')))
        .send()
        .await
        .map_err(|e| format!("Ollama connection failed: {}", e))?;

    let body = resp.text().await.map_err(|e| e.to_string())?;
    Ok(body)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_store::Builder::new().build())
        .plugin(tauri_plugin_updater::Builder::new().build())
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![check_server, check_ollama])
        .run(tauri::generate_context!())
        .expect("error while running KAOS");
}
