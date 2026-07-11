#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Scans the K.A.O.S codebase for mock/fabricated data patterns.
    Fails if any prohibited patterns are found.

.DESCRIPTION
    Enforces Constitution Article I: Zero Tolerance for Fabricated Data.
    Checks for:
      - Hardcoded VRAM values (vramTotal: 16, vramTotal: 8, etc.)
      - Static fallback arrays (fallbackAlerts, staticLogsSeeds)
      - _fallback_* functions that fabricate data
      - Static metrics seeds in dashboard/observability

.PARAMETER Path
    Root path of the K.A.O.S project. Defaults to current directory.

.EXAMPLE
    ./scripts/verify-no-mocks.ps1
    Scans the project for mock patterns.
#>

param(
    [string]$Path = (Get-Location).Path
)

$ErrorActionPreference = "Stop"
$exitCode = 0

# ── Patterns that indicate fabricated data ────────────────────────────

$mockPatterns = @(
    # Hardcoded VRAM values (Constitution violation)
    @{ Pattern = 'vramTotal:\s*1[0-9]'; Description = 'Hardcoded VRAM total value' },
    @{ Pattern = 'vramTotal:\s*[2-9][0-9]'; Description = 'Hardcoded VRAM total value' },

    # Static mock arrays
    @{ Pattern = 'fallbackAlerts'; Description = 'Static fallback alerts array' },
    @{ Pattern = 'staticLogsSeed'; Description = 'Static log seed data' },
    @{ Pattern = 'mockLogs'; Description = 'Mock log data' },
    @{ Pattern = 'fakeMetrics'; Description = 'Fake metrics data' },
    @{ Pattern = 'placeholderAlerts'; Description = 'Placeholder alerts' },
    @{ Pattern = 'dummyMetrics'; Description = 'Dummy metrics data' },

    # _fallback_ functions that fabricate data
    @{ Pattern = 'def _fallback_'; Description = 'Fallback function that fabricates data' },

    # VRAM fabrication patterns (single quotes and double quotes variants)
    @{ Pattern = 'vram.*\d+\.\d+\s*/\s*\d+GB'; Description = 'Fabricated VRAM string like "1.0/16GB"' }
)

# ── Files/Directories to exclude ──────────────────────────────────────

$excludePaths = @(
    '.git',
    'node_modules',
    '__pycache__',
    '.venv',
    'dist',
    'build',
    '.opencode',
    'graphify-out',
    'kaos-research',
    'airllm',
    'graphify',
    '.specify',
    'docs',
    'scripts'
)

$excludeExtensions = @(
    '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico',
    '.woff', '.woff2', '.ttf', '.eot',
    '.ico', '.pdf', '.lock',
    '.sum', '.sig', '.tar.gz', '.zip'
)

# ── Helper Functions ──────────────────────────────────────────────────

function Test-ShouldExclude {
    param([string]$FilePath)
    foreach ($excl in $excludePaths) {
        if ($FilePath -match [regex]::Escape($excl)) { return $true }
    }
    foreach ($ext in $excludeExtensions) {
        if ($FilePath -like "*$ext") { return $true }
    }
    return $false
}

function Test-MockPatterns {
    param([string]$FilePath)
    $content = Get-Content -Path $FilePath -Raw -ErrorAction SilentlyContinue
    if (-not $content) { return @() }

    $findings = @()
    foreach ($mock in $mockPatterns) {
        if ($content -match $mock.Pattern) {
            $lineNumber = 0
            $content -split "`n" | ForEach-Object {
                $lineNumber++
                if ($_ -match $mock.Pattern) {
                    $findings += [PSCustomObject]@{
                        File    = $FilePath
                        Line    = $lineNumber
                        Pattern = $mock.Pattern
                        Description = $mock.Description
                        Match   = $matches[0]
                    }
                }
            }
        }
    }
    return $findings
}

# ── Scan ──────────────────────────────────────────────────────────────

Write-Host "🔍 Scanning for mock/fabricated data patterns..." -ForegroundColor Cyan
Write-Host "Path: $Path`n" -ForegroundColor Gray

$allFindings = @()
$totalFiles = 0
$scannedFiles = 0

Get-ChildItem -Path $Path -Recurse -File | ForEach-Object {
    $totalFiles++
    if (-not (Test-ShouldExclude $_.FullName)) {
        $scannedFiles++
        $findings = Test-MockPatterns $_.FullName
        if ($findings.Count -gt 0) {
            $allFindings += $findings
        }
    }
}

# ── Results ───────────────────────────────────────────────────────────

Write-Host "Scanned $scannedFiles files (of $totalFiles total)" -ForegroundColor Gray

if ($allFindings.Count -eq 0) {
    Write-Host "`n✅ PASS: No mock/fabricated data patterns found." -ForegroundColor Green
    exit 0
}

Write-Host "`n❌ FAILED: $($allFindings.Count) mock/fabricated data patterns detected:`n" -ForegroundColor Red

$allFindings | Group-Object File | ForEach-Object {
    Write-Host "  📄 $($_.Name)" -ForegroundColor Yellow
    $_.Group | ForEach-Object {
        Write-Host "     Line $($_.Line): $($_.Description) — found '$($_.Match)'" -ForegroundColor Red
    }
}

Write-Host "`n⚠️  Remove all fabricated data before committing." -ForegroundColor Yellow
exit 1
