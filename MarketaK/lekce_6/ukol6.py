from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def wait_to_see(wait=3):
    time.sleep(wait)

# Test data
URL = "https://www.saucedemo.com/"
USERNAME = "problem_user"
PASSWORD = "secret_sauce"
EXPECTED_MENU_ITEMS = ["ALL ITEMS", "ABOUT", "LOGOUT", "RESET APP STATE"]


def setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def teardown():
    driver.quit()


def test_load_login_page(URL):
    try:
        driver.get(URL)
        assert "Swag Labs" in driver.title, f"Nejsme na správné stránce! titul: '{driver.current_url}'"
    except Exception as e:
        print(f"❌ Test selhal: {e}")


def test_login_user(username, password):
    try:
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        assert "inventory" in driver.current_url.lower()
        print("✅ Login test proběhl úspěšně – user je přihlášen na inventory stránce.")
    except Exception as e:
        print(f"❌ Test selhal: {e}")


def test_menu_items():
    try:
        wait_to_see(3)
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        menu_list = driver.find_elements(By.CLASS_NAME, "bm-item")
        assert len(menu_list) > 0, "Menu list is not displayed"
        found_items = [item.text for item in menu_list]

        for expected_item in EXPECTED_MENU_ITEMS:
            assert expected_item in found_items, f"Menu item '{expected_item}' not found in menu"

        print("✅ All expected menu items are present.")
        
    except Exception as e:
                print(f"❌ Test selhal: {e}")
    

# Running tests
setup()
test_load_login_page(URL)
test_login_user(USERNAME,PASSWORD)
test_menu_items()
teardown()