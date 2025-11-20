from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
from datetime import datetime
import os
from pagemodel.login import LoginPage

# Setup logging
script_dir = os.path.dirname(os.path.abspath(__file__))
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = os.path.join(script_dir, f"test_log_{timestamp}.log")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def wait_to_see(wait=3):
    """Pomocná funkce pro pauzu, aby bylo vidět, co se děje v prohlížeči."""
    logger.debug(f"wait_to_see called with wait={wait}")
    time.sleep(wait)

# Test data
URL = "https://www.saucedemo.com/"
USERNAME = "problem_user"
PASSWORD = "secret_sauce"

# Spuštění prohlížeče (Chrome přes WebDriver Manager)


def setup():
    logger.debug("setup called - initializing Chrome driver")
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    logger.info("Chrome driver initialized successfully")
   
def teardown():
    logger.debug("teardown called - quitting driver")
    driver.quit()
    logger.info("Driver quit successfully")


def test_login_user(URL, USERNAME, PASSWORD):
    try:
        login_page = LoginPage(driver)
        login_page.load(URL)
        login_page.login_user(USERNAME, PASSWORD)
    except Exception as e:
        logger.error(f"❌ Test 'load login page' selhal: {e}", exc_info=True)
        print(f"❌ Test 'load login page'selhal: {e}")


#XPATH /html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input
#//*[@id="user-name"]

logger.info("=== Starting test execution ===")
setup()
test_login_user(URL, USERNAME, PASSWORD)
teardown()
logger.info("=== Test execution completed ===")