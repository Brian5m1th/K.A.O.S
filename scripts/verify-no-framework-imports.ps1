#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Scans Desktop store files for direct framework imports.
    Fails if any store imports Graphify, Mem0, GraphRAG, LangGraph,
    Qdrant, or any framework directly instead of using K.A.O.S REST APIs.

.DESCRIPTION
    Enforces Architecture Fit Function: Desktop stores must never
    import or depend on framework libraries directly. All communication
    must go through K.A.O.S backend REST APIs.

.EXAMPLE
    ./scripts/verify-no-framework-imports.ps1
#>

param(
    [string]$StoresPath = "desktop/src/application/stores"
)

$ErrorActionPreference = "Stop"

$forbiddenImports = @(
    # Code intelligence
    "graphify", "graphifyy",
    # Knowledge / Memory
    "mem0", "mem0ai", "graphiti", "graphrag", "cognee",
    # Agent orchestration
    "langgraph", "letta", "crewai", "autogen",
    # Vector / Graph DB
    "qdrant", "qdrant-client", "falkordb", "neo4j", "networkx",
    # LLM / Inference
    "airllm", "langchain", "transformers", "torch",
    # Observability
    "langfuse", "opentelemetry"
)

Write-Host "🔍 Scanning Desktop stores for forbidden framework imports..." -ForegroundColor Cyan

$findings = @()

Get-ChildItem -Path $StoresPath -Filter "*.ts" -Recurse | ForEach-Object {
    $content = Get-Content $_.FullName -Raw

    foreach ($imp in $forbiddenImports) {
        if ($content -match "from\s+['`"].*${imp}.*['`"]" -or
            $content -match "require\s*\(.*${imp}.*\)" -or
            $content -match "import\s+.*\s+from\s+['`"].*${imp}.*['`"]") {

            $findings += [PSCustomObject]@{
                File      = $_.FullName
                Framework = $imp
                Message   = "Direct import of framework '$imp' detected — use K.A.O.S REST API instead"
            }
        }
    }
}

if ($findings.Count -eq 0) {
    Write-Host "✅ PASS: No forbidden framework imports in Desktop stores." -ForegroundColor Green
    exit 0
}

Write-Host "`n❌ FAILED: $($findings.Count) forbidden framework import(s) detected:`n" -ForegroundColor Red

$findings | Group-Object File | ForEach-Object {
    Write-Host "  📄 $($_.Name)" -ForegroundColor Yellow
    $_.Group | ForEach-Object {
        Write-Host "     → $($_.Message)" -ForegroundColor Red
    }
}

Write-Host "`n⚠️  Replace direct framework imports with K.A.O.S REST API calls." -ForegroundColor Yellow
exit 1
