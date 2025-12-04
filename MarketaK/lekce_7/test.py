import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pagemodel.login_page import LoginPage
from pagemodel.inventory_page import InventoryPage


#LOGGING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# SETUP
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    logging.info("Browser started.")
    return driver


# TEARDOWN 
def teardown(driver):
    logging.info("Closing browser.")
    driver.quit()


#  ACTUAL TEST 
driver = setup()

try:
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    logging.info("Opening login page.")
    login.open()

    logging.info("Logging in as standard_user.")
    login.login("standard_user", "secret_sauce")

    logging.info("Adding backpack to cart.")
    inventory.add_backpack_to_cart()

    assert inventory.is_in_cart(), " Backpack was NOT added to cart!"
    logging.info("✔ Backpack successfully added to cart.")

except AssertionError as ae:
    logging.error(f"ASSERT FAILED: {ae}")
    raise

except Exception as e:
    logging.error(f"UNEXPECTED ERROR: {e}")
    raise

finally:
    teardown(driver)

