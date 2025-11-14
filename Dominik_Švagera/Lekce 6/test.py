from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

def test_product_filters():
    logger.debug("test_product_filters called")
    print()
    try:

        filter_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        
       
        filter_options = filter_dropdown.options
        filter_names = [option.text for option in filter_options]
        
        logger.info(f"Nalezeno {len(filter_names)} možností filtrování: {', '.join(filter_names)}")
        
        for option in filter_options:
            filter_name = option.text
            filter_value = option.get_attribute("value")
            
            filter_dropdown.select_by_value(filter_value)
            wait_to_see(1)

            selected_option = filter_dropdown.first_selected_option
            assert selected_option.text == filter_name, f"Filtr '{filter_name}' nebyl správně aplikován!"
            
            logger.debug(f"Filtr '{filter_name}' úspěšně aplikován")
            
            products = driver.find_elements(By.CLASS_NAME, "inventory_item")
            assert len(products) > 0, f"Po aplikaci filtru '{filter_name}' se nezobrazují žádné produkty!"
            
        message = f"✅ Test filtrů proběhl úspěšně – otestováno {len(filter_names)} filtrů: {', '.join(filter_names)}."
        logger.info(message)
        print(message)
    except Exception as e:
        logger.error(f"❌ Test 'product filters' selhal: {e}", exc_info=True)
        print(f"❌ Test 'product filters' selhal: {e}")

def test_add_all_products_to_cart():
    logger.debug("test_add_all_products_to_cart called")
    print()
    try:
        add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, "button[id^='add-to-cart']")
        products_count = len(add_to_cart_buttons)
        
        assert products_count > 0, "Nebyly nalezeny žádné produkty k přidání do košíku!"
        
        for button in add_to_cart_buttons:
            product_name = button.get_attribute("id").replace("add-to-cart-", "")
            button.click()
            logger.debug(f"Produkt '{product_name}' přidán do košíku")
            wait_to_see(0.5)
        
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        cart_count = int(cart_badge.text)
        
        assert cart_count == products_count, f"V košíku je {cart_count} položek, očekáváno bylo {products_count}!"
        
        message = f"✅ Test přidání produktů do košíku proběhl úspěšně – přidáno {products_count} produktů."
        logger.info(message)
        print(message)
    except Exception as e:
        logger.error(f"❌ Test 'add all products to cart' selhal: {e}", exc_info=True)
        print(f"❌ Test 'add all products to cart' selhal: {e}")

def test_verify_cart_contents():
    logger.debug("test_verify_cart_contents called")
    print()
    try:
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        wait_to_see(1)
        
        assert "cart" in driver.current_url.lower(), "Nejsme na stránce košíku!"
        
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        items_count = len(cart_items)
        
        assert items_count > 0, "Košík je prázdný, ale měl by obsahovat produkty!"
        
        product_names = []
        for item in cart_items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            product_names.append(name)
            logger.debug(f"V košíku je produkt: {name}")
        
        message = f"✅ Test ověření košíku proběhl úspěšně – košík obsahuje {items_count} produktů: {', '.join(product_names)}."
        logger.info(message)
        print(message)
    except Exception as e:
        logger.error(f"❌ Test 'verify cart contents' selhal: {e}", exc_info=True)
        print(f"❌ Test 'verify cart contents' selhal: {e}")


logger.info("=== Starting test execution ===")
setup()
test_load_login_page(URL)
test_login_user(USERNAME, PASSWORD)
test_product_filters()
test_add_all_products_to_cart()
test_verify_cart_contents()
teardown()
logger.info("=== Test execution completed ===")