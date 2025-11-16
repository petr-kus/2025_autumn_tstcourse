Write-Host "=== Creating virtual environment ==="
py -m venv venv

Write-Host "=== Activating virtual environment ==="
.\venv\Scripts\Activate.ps1

Write-Host "=== Installing required Python packages ==="
pip install selenium
pip install webdriver-manager

Write-Host "=== Saving packages to requirements.txt ==="
pip freeze > requirements.txt

Write-Host "=== Done! ==="
Write-Host "To start working, activate your venv using:"
Write-Host "   .\venv\Scripts\Activate.ps1"
