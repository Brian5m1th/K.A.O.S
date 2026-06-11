param(
    [int]$Port = 8000,
    [switch]$Reload = $true
)

$reload_arg = if ($Reload) { "--reload" } else { "" }
$app_dir = Resolve-Path "$PSScriptRoot/.."

uv run --directory $app_dir uvicorn app.main:app $reload_arg --port $Port
