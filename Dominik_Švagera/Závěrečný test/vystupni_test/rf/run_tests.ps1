# Robot Framework execution script
# Runs all Robot Framework tests with HTML reports

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Running Robot Framework Tests" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

py -3.14 -m robot -d logs test_web_app.robot

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Test execution completed" -ForegroundColor Cyan
Write-Host "Check logs directory for reports:" -ForegroundColor Cyan
Write-Host "  - log.html (detailed test log)" -ForegroundColor White
Write-Host "  - report.html (test report)" -ForegroundColor White
Write-Host "  - output.xml (test output)" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
