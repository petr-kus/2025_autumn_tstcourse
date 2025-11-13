from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

# login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# ASSERT 1: správná URL
assert "inventory" in driver.current_url

# ASSERT 2: titulek stránky
assert "Swag Labs" in driver.title

# ASSERT 3: zkontroluj viditelnost nějakého prvku
inventory_container = driver.find_element(By.ID, "inventory_container")
assert inventory_container.is_displayed()

# extra klik – klikni na první produkt
first_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
first_item.click()

time.sleep(5)

driver.quit()

