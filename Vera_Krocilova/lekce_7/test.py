from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pagemodel.login_page import LoginPage
from pagemodel.inventory_page import InventoryPage
import logging


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
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
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
        logging.info(f"Random product '{random_product}' selected successfully.")

        added_random_product = inventory_page.add_to_cart(random_product)
        logging.info(f"Random product '{added_random_product}' added to cart.")
       
        cart_count = inventory_page.cart_count()
        assert cart_count == 1, f"Cart count expected to be 1 but got {cart_count}."
        logging.info("Cart count verified successfully.")
        
        inventory_page.go_to_cart()
        assert "cart" in driver.current_url.lower(), "Failed to navigate to cart page."
        logging.info("Navigated to cart page.")

        driver.back()
        
        return random_product

    except Exception as e:
        logging.error(f"Test failed: {e}")
        

def test_click_product_image(random_product):
    try:
        inventory_page = InventoryPage(driver)
                
        random_product = inventory_page.choose_random_product(inventory_page.display_products())
        selected_image_src = inventory_page.click_product_image(random_product)
        detail_image_src = inventory_page.get_detail_image_src()
        assert selected_image_src is not None, "Failed to get selected product image src."
        assert selected_image_src == detail_image_src, (f"Expected image src {selected_image_src} but got {detail_image_src}.") 
        logging.info("Product image displayed successfully.")

        driver.back()
       
    except Exception as e:
        logging.error(f"Test failed: {e}")
        

def test_click_product_name(random_product):
    try:
        inventory_page = InventoryPage(driver)
        
        random_product = inventory_page.choose_random_product(inventory_page.display_products())
        selected_name = inventory_page.click_product_name(random_product)
        detail_name = inventory_page.get_detail_name()
        assert selected_name == detail_name, (f"Expected product {selected_name} but got {detail_name}.")
        logging.info("Product details displayed successfully.")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        

def teardown():
    driver.quit()
    logging.info("Browser closed.")


setup_logging()
setup()
test_login_page("https://www.saucedemo.com/", "standard_user", "secret_sauce")
random_product = test_add_to_cart()
test_click_product_image(random_product)
test_click_product_name(random_product)
teardown()

