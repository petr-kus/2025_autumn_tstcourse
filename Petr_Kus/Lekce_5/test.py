from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def wait_to_see(wait=3):
    """Pomocná funkce pro pauzu, aby bylo vidět, co se děje v prohlížeči."""
    time.sleep(wait)

# Test data
URL = "https://www.saucedemo.com/"
USERNAME = "problem_user"
PASSWORD = "secret_sauce"

# Spuštění prohlížeče (Chrome přes WebDriver Manager)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait_to_see()
# 1) Otevřeme login stránku
driver.get(URL)
wait_to_see()
# Ověříme, že jsme fakt na Swag Labs (kontrola titulku)
assert "Swag Labs" in driver.title, f"Nejsme na správné stránce! Jsme nyni na strance '{driver.title}'"

# 2) Najdeme prvky na stránce (lokátory)
username_input = driver.find_element(By.ID, "user-name")
#XPATH /html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input
#//*[@id="user-name"]
#selector #user-name

password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# 3) Vyplníme login formulář
wait_to_see()
username_input.send_keys(USERNAME)
wait_to_see()
password_input.send_keys(PASSWORD)
wait_to_see()

# 4) Odeslání formuláře (klik na Login)
login_button.click()
wait_to_see()
# 5) Ověření úspěšného loginu
# Po úspěšném přihlášení jsme na /inventory.html a vidíme produkty
assert "inventory" in driver.current_url.lower()

# Zkusíme najít nějaký typický prvek na stránce – např. container s produkty
inventory_container = driver.find_elements(By.C, "inventory_container")
assert inventory_container.is_displayed()

print(f"✅ Login test proběhl úspěšně – user '{USERNAME}' je přihlášen na inventory stránce '{driver.current_url}'.")
wait_to_see(10)
driver.quit()