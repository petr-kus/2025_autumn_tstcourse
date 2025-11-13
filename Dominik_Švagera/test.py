from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
from datetime import datetime
import os

log_filename = f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_filepath = os.path.join(os.path.dirname(__file__), log_filename)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

URL = "https://www.saucedemo.com/"
USERNAME = "problem_user"
PASSWORD = "secret_sauce"

def setup():
    logger.debug(f"setup() called with no input parameters")
    global driver 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    logger.info("Browser setup completed successfully")


def teardown():
    logger.debug(f"teardown() called with no input parameters")
    driver.quit()
    logger.info("Browser teardown completed successfully")

def load_login_page():
    logger.debug(f"load_login_page() called with no input parameters")
    try:
        driver.get(URL)
        logger.info(f"Navigated to URL: {URL}")
        assert "Swag Labs" in driver.title, f"Expected title to contain 'Swag Labs' but got '{driver.title}'"
        logger.info(f"Page title verification passed: {driver.title}")
    except Exception as e:
        logger.error(f"Failed to load login page. Error: {e}", exc_info=True)
        print(f"Failed to load login page. Error: {e}")
    
def test_login_user(username, password):
    logger.debug(f"test_login_user() called with input data - username: {username}, password: {'*' * len(password)}")
    logger.info(f"Testing login for user: {username}")
    print(f"Testing login for user: {username}")
    try:
        driver.find_element(By.ID, "user-name")
        driver.find_element(By.ID, "password")
        driver.find_element(By.ID, "login-button").click()
        logger.info("Login button clicked")
        assert "inventory" in driver.current_url.lower(), "Login failed, inventory page not reached!"
        logger.info(f"Login successful, current URL: {driver.current_url}")
    except Exception as e:
        logger.error(f"Login test failed for user: {username}. Error: {e}", exc_info=True)
        print(f"Login test failed for user: {username}. Error: {e}")


def test_product_texts_visible():
    logger.debug(f"test_product_texts_visible() called with no input parameters")
    try:
        driver.get(URL)
        logger.info(f"Navigated to URL: {URL}")
        driver.find_element(By.ID, "user-name").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        logger.info(f"Credentials entered for user: {USERNAME}")
        driver.find_element(By.ID, "login-button").click()
        logger.info("Login button clicked")
        
        inventory_container = driver.find_element(By.ID, "inventory_container")
        assert inventory_container.is_displayed(), "Inventory container is not displayed!"
        logger.info("Inventory container is displayed")
        
        product_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        assert len(product_names) > 0, "No products were found on the page!"
        logger.info(f"Found {len(product_names)} products on the page")
        
        for product in product_names:
            assert product.is_displayed(), f"Product {product.text} is not visible!"
            assert product.text.strip() != "", "Product name is empty!"
            logger.info(f"Product verified: {product.text}")
        
        logger.info("All products are visible and have valid names")
    except Exception as e:
        logger.error(f"Product visibility test failed. Error: {e}", exc_info=True)
        raise

logger.info("========== Test execution started ==========")
setup()
load_login_page(URL)
test_login_user(USERNAME, PASSWORD)
test_product_texts_visible()
teardown()
logger.info("========== Test execution completed ==========")
