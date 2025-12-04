import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# Testovací data
URL = "https://www.saucedemo.com/"  
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture(autouse=True, scope="session")
def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')    

@pytest.fixture(autouse=True, scope="session")
def browser():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--guest")
    prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,
            }
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    logging.info("Browser initialized and maximized.")
    yield driver
    driver.quit()

    logging.info("Browser closed.")


@pytest.fixture
def logged_in_inventory_page(browser):  
    login_page = LoginPage(browser)
    login_page.load(URL)
    login_page.login_user(USERNAME, PASSWORD)
    inventory_page = InventoryPage(browser)
    return inventory_page


@pytest.fixture 
def any_product(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page
    product = inventory_page.choose_random_product(inventory_page.display_products())
    logging.info(f"Selected product for test: '{product.text}'")
    return product


  
