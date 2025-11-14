from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
from datetime import datetime
import os

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

def test_load_login_page(URL):
    logger.debug(f"test_load_login_page called with URL={URL}")
    try:
        driver.get(URL)
        assert "Swag Labs" in driver.title, f"Nejsme na správné stránce! Jsme nyni na strance '{driver.title}'"
        logger.info(f"✅ Login page loaded successfully - title: {driver.title}")
    except Exception as e:
        logger.error(f"❌ Test 'load login page' selhal: {e}", exc_info=True)
        print(f"❌ Test 'load login page'selhal: {e}")

def test_login_user(username, password):
    logger.debug(f"test_login_user called with username={username}, password={'*' * len(password)}")
    print()
    try:
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        assert "inventory" in driver.current_url.lower(), "Login failed!"
        message = f"✅ Login test proběhl úspěšně – user '{USERNAME}' je přihlášen nva inentory stránce '{driver.current_url}'."
        logger.info(message)
        print(message)
    except Exception as e:
        logger.error(f"❌ Test 'login user' selhal: {e}", exc_info=True)
        print(f"❌ Test 'login user'selhal: {e}")


logger.info("=== Starting test execution ===")
setup()
test_load_login_page(URL)
test_login_user(USERNAME, PASSWORD)
teardown()
logger.info("=== Test execution completed ===")