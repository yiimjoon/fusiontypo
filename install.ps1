$ErrorActionPreference = "Stop"

$sourceDir = Join-Path $PSScriptRoot "package\\Edit"
$targetDir = Join-Path $env:APPDATA "Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Templates\\Edit"
$distDir = Join-Path $PSScriptRoot "dist"
$drfx = Join-Path $distDir "Codex-Rise-Fade.drfx"
$zipPath = Join-Path $distDir "Codex-Rise-Fade.zip"

if (!(Test-Path $sourceDir)) {
    throw "Preset folder not found: $sourceDir"
}

New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
New-Item -ItemType Directory -Force -Path $distDir | Out-Null

Copy-Item -Path (Join-Path $sourceDir "*") -Destination $targetDir -Recurse -Force

if (Test-Path $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}

if (Test-Path $drfx) {
    Remove-Item -LiteralPath $drfx -Force
}

Compress-Archive -Path $sourceDir -DestinationPath $zipPath -Force
Rename-Item -LiteralPath $zipPath -NewName (Split-Path $drfx -Leaf)

Write-Host "Installed presets to:"
Write-Host "  $targetDir\\Titles\\Codex Rise Fade.setting"
Write-Host "  $targetDir\\Titles\\Codex Rise Fade Pro.setting"
Write-Host ""
Write-Host "Created DRFX package:"
Write-Host "  $drfx"
Write-Host ""
Write-Host "Restart DaVinci Resolve or refresh Effects Library to see both presets under Titles."
