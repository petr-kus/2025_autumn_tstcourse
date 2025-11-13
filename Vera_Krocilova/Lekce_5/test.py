from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Spuštění prohlížeče (použijeme Chrome)
driver = webdriver.Chrome()

# 1️⃣ Otevřeme testovací stránku
driver.get("https://www.saucedemo.com/")

# 2️⃣ Najdeme pole pro uživatelské jméno a heslo
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")

# 3️⃣ Zadáme testovací údaje (funkční demo přihlášení)
username.send_keys("standard_user")
password.send_keys("secret_sauce")
password.send_keys(Keys.RETURN)

# 4️⃣ Počkáme krátce, aby se stránka načetla
time.sleep(2)

# 5️⃣ Ověříme, že přihlášení proběhlo – např. podle textu na stránce
if "inventory" in driver.current_url:
    print("✅ Test prošel: Přihlášení bylo úspěšné.")
else:
    print("❌ Test neprošel: Přihlášení se nezdařilo.")

# 6️⃣ Zavřeme prohlížeč
driver.quit()
