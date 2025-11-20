from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import logging

def wait_to_see():
    time.sleep(1)


#test data
URL = "https://www.saucedemo.com/"
USERNAME = "problem_user"
PASSWORD = "secret_sauce"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()


def test_load_login_page():
    try:
        driver.get(URL)
        assert driver.current_url == "https://www.saucedemo.com/", f"Incorrect page loaded. Current url: '{driver.current_url}'"
        print("✅ Test passed: Login page loaded successfully.")
    except Exception as e:
        logging.error(f"❌ Test failed: {e}")
        raise


def test_login(username, password):
    user_field = driver.find_element(By.ID, "user-name")
    pass_field = driver.find_element(By.ID, "password")
    user_field.send_keys(username)
    pass_field.send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url.lower(), "Login failed!"
    logging.info("✅ Test passed: Login successful.")


def test_add_to_cart():
    wait_to_see()

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No products found on inventory page!"

    random_product = random.choice(products)
    add_button = random_product.find_element(By.TAG_NAME, "button")

    add_button.click()
    wait_to_see()

    try:
        badges = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    except:
        raise AssertionError("No cart badge found after adding product to cart! (expected bug for problem_user)")

    cart_count = badges.text.strip()
    assert cart_count == "1", f"Product was not added to cart! Cart count: {cart_count}"

    print("✅ Test passed: Product added to cart successfully.")
    
      
def teardown():
    driver.quit()


setup()
test_load_login_page()
test_login(USERNAME, PASSWORD)
test_add_to_cart()
teardown()