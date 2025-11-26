# Script de Migração do NeoSigm Genesis (Robocopy Version)
# Este script copia o projeto atual para a pasta de projetos oficial usando Robocopy.

$ErrorActionPreference = "Continue" # Robocopy returns non-zero exit codes for success

$sourcePath = Get-Location
$targetParent = "C:\Users\João\Desktop\PROJETOS"
$targetName = "NeoSigm_Genesis"
$targetPath = Join-Path $targetParent $targetName

Write-Host "🚀 Iniciando migração do NeoSigm Genesis (via Robocopy)..." -ForegroundColor Cyan
Write-Host "📂 Origem: $sourcePath"
Write-Host "📂 Destino: $targetPath"

# Garante que o diretório pai existe
if (-not (Test-Path $targetParent)) {
    New-Item -ItemType Directory -Force -Path $targetParent | Out-Null
}

# Define exclusões (pastas temporárias e de sistema)
$excludeDirs = @("venv", "__pycache__", ".git", ".gemini", ".idea", ".vscode")

# Executa Robocopy
Write-Host "📦 Copiando arquivos..." -ForegroundColor Cyan

# Robocopy arguments need to be passed individually
$robocopyArgs = @($sourcePath, $targetPath, "/E", "/R:0", "/W:0", "/NFL", "/NDL", "/XD") + $excludeDirs

& robocopy $robocopyArgs

# Verifica o código de saída do Robocopy (qualquer coisa < 8 é sucesso/aviso)
if ($LASTEXITCODE -lt 8) {
    Write-Host "✅ Migração concluída com sucesso!" -ForegroundColor Green
    Write-Host "👉 Agora você pode abrir o projeto em: $targetPath" -ForegroundColor White
} else {
    Write-Host "❌ Houve erros durante a cópia. Código de saída: $LASTEXITCODE" -ForegroundColor Red
}
