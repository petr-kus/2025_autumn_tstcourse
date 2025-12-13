# Installation script for SauceDemo test automation dependencies
# This script installs all required Python packages for both PyTest and Robot Framework tests

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "SauceDemo Test Automation - Dependency Installation" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: Python is not installed or not in PATH!" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Check if pip is installed
Write-Host "Checking pip installation..." -ForegroundColor Yellow
try {
    $pipVersion = pip --version 2>&1
    Write-Host "Found: $pipVersion" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: pip is not installed!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Installing PyTest dependencies..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Set-Location "$PSScriptRoot\pytest"
if (Test-Path "requirements.txt") {
    Write-Host "Installing from pytest/requirements.txt..." -ForegroundColor Yellow
    pip install -r requirements.txt
    if ($LASTEXITCODE -eq 0) {
        Write-Host "PyTest dependencies installed successfully!" -ForegroundColor Green
    }
    else {
        Write-Host "ERROR: Failed to install PyTest dependencies!" -ForegroundColor Red
        exit 1
    }
}
else {
    Write-Host "ERROR: pytest/requirements.txt not found!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Installing Robot Framework dependencies..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Set-Location "$PSScriptRoot\rf"
if (Test-Path "requirements.txt") {
    Write-Host "Installing from rf/requirements.txt..." -ForegroundColor Yellow
    pip install -r requirements.txt
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Robot Framework dependencies installed successfully!" -ForegroundColor Green
    }
    else {
        Write-Host "ERROR: Failed to install Robot Framework dependencies!" -ForegroundColor Red
        exit 1
    }
}
else {
    Write-Host "ERROR: rf/requirements.txt not found!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Verifying installations..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Set-Location $PSScriptRoot

Write-Host ""
Write-Host "PyTest version:" -ForegroundColor Yellow
pytest --version

Write-Host ""
Write-Host "Robot Framework version:" -ForegroundColor Yellow
robot --version

Write-Host ""
Write-Host "Selenium version:" -ForegroundColor Yellow
pip show selenium | Select-String "Version"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Installation completed successfully!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "You can now run the tests:" -ForegroundColor Cyan
Write-Host "  PyTest:          cd vystupni_test\pytest; pytest" -ForegroundColor White
Write-Host "  Robot Framework: cd vystupni_test\rf; robot test_saucedemo.robot" -ForegroundColor White
Write-Host ""
