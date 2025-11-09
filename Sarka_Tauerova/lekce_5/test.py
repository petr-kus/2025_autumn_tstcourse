from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Test data
URL = "https://www.saucedemo.com/"
USERNAME = "problem_user"
PASSWORD = "secret_sauce"

# Spuštění prohlížeče (Chrome přes WebDriver Manager)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1) Otevřeme login stránku
driver.get(URL)

# Ověříme, že jsme fakt na Swag Labs (kontrola titulku)
assert "Swag Labs" in driver.title

# 2) Najdeme prvky na stránce (lokátory)
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# 3) Vyplníme login formulář
username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)

# 4) Odeslání formuláře (klik na Login)
login_button.click()

# 5) Ověření úspěšného loginu
# Po úspěšném přihlášení jsme na /inventory.html a vidíme produkty
assert "inventory" in driver.current_url.lower()

# Zkusíme najít nějaký typický prvek na stránce – např. container s produkty
inventory_container = driver.find_element(By.ID, "inventory_container")
assert inventory_container.is_displayed()

print("✅ Login test proběhl úspěšně – user je přihlášen na inventory stránce.")

driver.quit()