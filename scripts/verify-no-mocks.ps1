#!/usr/bin/env pwsh
<#
.SYNOPSIS
  Production mock audit — scans the K.A.O.S codebase for fabricated/mock runtime data patterns.
.DESCRIPTION
  Exits 0 if no illegal mock patterns are found in production code.
  Exits 1 if any mock data markers are detected.
  Exempts: unit tests (src/__tests__/), layout-engine.ts (layout jitter), UUID polyfills.
#>

$ErrorActionPreference = "Stop"
$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Resolve-Path "$ScriptRoot\.."
$ExitCode = 0
$Violations = @()

$mockPatterns = @(
    @{ Pattern = "fallbackAlerts";   Desc = "Fallback alert array" },
    @{ Pattern = "simulatedLogs";    Desc = "Simulated log entries" },
    @{ Pattern = "DEFAULT_AGENTS";   Desc = "Hardcoded default agents" },
    @{ Pattern = "INITIAL_NODES";    Desc = "Hardcoded workflow nodes" },
    @{ Pattern = "INITIAL_EDGES";    Desc = "Hardcoded workflow edges" },
    @{ Pattern = "mock_fallback";    Desc = "Mock fallback data (backend)" },
    @{ Pattern = "SIMULATED";        Desc = "Simulated data badge/marker" },
    @{ Pattern = "simular|simulado|simulate"; Desc = "Simulation comments/logic" },
    @{ Pattern = "fallback\s*simul"; Desc = "Fallback simulation" },
    @{ Pattern = "fakeAlerts";       Desc = "Fake alerts array" },
    @{ Pattern = "dummy";            Desc = "Dummy data marker" }
)

$exemptDirs = @("__tests__", "tests", "__pycache__", "node_modules", ".git", ".venv", "dist", "target", ".idea")
$exemptFiles = @("layout-engine.ts", "tool-schema.ts", "verify-no-mocks.ps1")
# layout-engine.ts exempt: Math.random used for graph layout jitter (visual only, not operational data)
# tool-schema.ts exempt: Math.random used as crypto.randomUUID() fallback for ID generation

Write-Host "=== K.A.O.S Production Mock Audit ===" -ForegroundColor Cyan
Write-Host "Project root: $ProjectRoot`n"

Get-ChildItem -Path $ProjectRoot -Recurse -Include "*.ts","*.tsx","*.py","*.js","*.json" -Exclude "*.d.ts" |
    Where-Object {
        $file = $_.FullName
        $exempt = $false
        foreach ($dir in $exemptDirs) {
            if ($file -match "[\\/]$dir[\\/]") { $exempt = $true; break }
        }
        foreach ($ef in $exemptFiles) {
            if ($file -like "*$ef") { $exempt = $true; break }
        }
        -not $exempt
    } |
    ForEach-Object {
        $file = $_
        $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
        if (-not $content) { return }

        foreach ($entry in $mockPatterns) {
            if ($content -match $entry.Pattern) {
                $lineNum = 0
                $content -split "`n" | ForEach-Object {
                    $lineNum++
                    if ($_ -match $entry.Pattern) {
                        # Skip false positives (comments about mock removal, test setup descriptions)
                        if ($_ -match "verify-no-mocks|should not contain|mock data detected|audit.*mock|eliminar|remove mocks|no mock|mock removal") {
                            continue
                        }
                        $shortFile = $file.FullName.Replace($ProjectRoot, "").TrimStart("\","/")
                        $violation = "$shortFile`:$lineNum  [$($entry.Desc)] $_"
                        $Violations += $violation
                    }
                }
            }
        }
    }

if ($Violations.Count -eq 0) {
    Write-Host "PASS: No illegal mock data patterns detected in production code." -ForegroundColor Green
    exit 0
}
else {
    Write-Host "FAIL: Found $($Violations.Count) mock data pattern(s) in production code:" -ForegroundColor Red
    $Violations | ForEach-Object { Write-Host "  $_" -ForegroundColor Red }
    Write-Host "`nThese patterns must be removed for production readiness." -ForegroundColor Yellow
    Write-Host "If the pattern is legitimate (test only, layout engine, UUID gen), add an exemption." -ForegroundColor Yellow
    exit 1
}
