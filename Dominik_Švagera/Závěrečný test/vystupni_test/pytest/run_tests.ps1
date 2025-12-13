# PyTest execution script
# Runs all PyTest tests with proper logging configuration

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Running PyTest Tests" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

py -3.14 -m pytest -v

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Test execution completed" -ForegroundColor Cyan
Write-Host "Check logs directory for detailed logs" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
