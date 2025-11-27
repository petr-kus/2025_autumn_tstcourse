from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pagemodel.login_page import LoginPage
from pagemodel.inventory_page import InventoryPage
import logging
import time


def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')    


def setup():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--guest")
    prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,
            }
    options.add_experimental_option("prefs", prefs)
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(2)
    logging.info("Browser initialized and maximized.")

def test_login_page(URL, USERNAME, PASSWORD):
    try:
        login_page = LoginPage(driver)

        login_page.load(URL)
        assert driver.current_url == URL, f"Incorrect page loaded. Current url: '{driver.current_url}'"
        logging.info("Login page loaded successfully.")

        login_page.login_user(USERNAME, PASSWORD)
        assert "inventory" in driver.current_url.lower(), "Login failed!"
        logging.info("Login successful.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        raise


def test_add_to_cart():
    try:
        inventory_page = InventoryPage(driver)
        
        displayed_all_products = inventory_page.display_products()
        assert len(displayed_all_products) > 0, "No products found on inventory page!"
        logging.info(f"Found {len(displayed_all_products)} products on inventory page.")

        random_product = inventory_page.choose_random_product(displayed_all_products)
        assert random_product is not None, "Failed to select a random product."
        logging.info("Random product selected successfully.")

        added_random_product = inventory_page.add_to_cart(random_product)
        logging.info(f"Random product '{inventory_page.last_added_product_name}' added to cart.")

        cart_count = inventory_page.cart_count()
        assert cart_count == 1, f"Cart count expected to be 1 but got {cart_count}."
        logging.info("Cart count verified successfully.")

        go_to_cart = inventory_page.go_to_cart()
        assert "cart" in driver.current_url.lower(), "Failed to navigate to cart page."
        logging.info("Navigated to cart page.")

        return random_product

    except Exception as e:
        logging.error(f"Test failed: {e}")
        raise


def test_display_item_image(random_product):
    try:
        inventory_page = InventoryPage(driver)
        
        image_product = inventory_page.display_image_item(random_product)
        assert "sauce" in image_product, "Failed to display product image."
        assert "labs" in image_product, "Failed to display product image."
        logging.info("Product image displayed successfully.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        raise


def test_display_details_item(random_product):
    try:
        inventory_page = InventoryPage(driver)

        name_product = inventory_page.display_details_item(random_product)
        assert "Sauce" in name_product, "Failed to display product details."
        assert "Bike" in name_product, "Failed to display product details."
        logging.info("Product details displayed successfully.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        raise

def teardown():
    driver.quit()
    logging.info("Browser closed.")


setup_logging()
setup()
test_login_page("https://www.saucedemo.com/", "standard_user", "secret_sauce")
random_product = test_add_to_cart()
test_display_item_image(random_product)
test_display_details_item(random_product)
teardown()

