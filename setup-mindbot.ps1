# MINDBOT Office Setup Script
# Run this once to fully configure the office

Write-Host "🌀 Setting up M1NDB0T Office..." -ForegroundColor Cyan

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$stateFile = Join-Path $projectRoot "state.json"

# Update state with MINDBOT branding
$state = @{
    state = "idle"
    detail = "M1NDB0T Online - Mind Expansion HQ"
    progress = 0
    updated_at = (Get-Date -Format "o")
    agent_name = "M1NDB0T"
    office_name = "Mind Expansion Network HQ"
} | ConvertTo-Json -Depth 5

$state | Out-File -FilePath $stateFile -Encoding utf8
Write-Host "✓ State file configured" -ForegroundColor Green

# Start backend
Write-Host "🚀 Starting backend server..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$projectRoot\backend'; python app.py"
Write-Host "✓ Backend starting on http://127.0.0.1:19000" -ForegroundColor Green

Write-Host "`n🏠 M1NDB0T Office is ready!" -ForegroundColor Cyan
Write-Host "Open: http://127.0.0.1:19000" -ForegroundColor Yellow
Write-Host "`nQuick status commands:" -ForegroundColor Cyan
Write-Host "  python set_state.py idle `"Standing by`""
Write-Host "  python set_state.py writing `"Building something`""
Write-Host "  python set_state.py researching `"Looking up docs`""
Write-Host "  python set_state.py syncing `"Deploying`""
Write-Host "  python set_state.py error `"Debugging`""
