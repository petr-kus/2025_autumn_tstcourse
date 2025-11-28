Write-Host "=== Creating virtual environment ==="
py -m venv venv

Write-Host "=== Activating virtual environment ==="
# Aktivace v rámci skriptu – upravíme PATH a proměnnou VIRTUAL_ENV
$env:VIRTUAL_ENV = (Resolve-Path ".\venv").Path
$env:PATH = "$env:VIRTUAL_ENV\Scripts;" + $env:PATH
Write-Host "Virtual environment activated."

Write-Host "=== Upgrading pip ==="
python -m pip install --upgrade pip

Write-Host "=== Installing required Python packages ==="
pip install selenium
pip install webdriver-manager
pip install pytest

Write-Host "=== Saving installed packages to requirements.txt ==="
pip freeze > requirements.txt

Write-Host ""
Write-Host "=== Setup completed successfully! ==="
Write-Host "Virtual environment is active."
Write-Host "To activate it manually next time, use:"
Write-Host "   .\venv\Scripts\Activate.ps1"
Write-Host ""

