param(
    [int]$Port = 8000,
    [switch]$Reload = $true
)

$reload_arg = if ($Reload) { "--reload" } else { "" }
$app_dir = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)

uv run uvicorn app.main:app $reload_arg --port $Port --app-dir $app_dir
