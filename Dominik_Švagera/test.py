from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.saucedemo.com/"
USERNAME = "problem_user"
PASSWORD = "secret_sauce"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get(URL)


assert "Swag Labs" in driver.title

username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)

login_button.click()

assert "inventory" in driver.current_url.lower()

inventory_container = driver.find_element(By.ID, "inventory_container")
assert inventory_container.is_displayed()

print("Login was successful and inventory page is displayed.")

product_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
assert len(product_names) > 0, "No products were found on the page!"

for product in product_names:
    assert product.is_displayed(), f"Product {product.text} is not visible!"
    assert product.text.strip() != "", "Product name is empty!"

print("All product texts are visible to the user.")

driver.quit()