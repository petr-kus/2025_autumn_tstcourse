from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)


class LoginPage:
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logger.debug(f"LoginPage initialized with driver: {driver}")

    def open(self, url):
        logger.info(f"Opening login page: {url}")
        self.driver.get(url)
        logger.debug(f"Current URL after navigation: {self.driver.current_url}")
        return self

    def verify_page_loaded(self):
        logger.debug(f"Verifying page loaded - current title: {self.driver.title}")
        assert "Swag Labs" in self.driver.title
        logger.info("Login page loaded successfully")
        return self

    def login(self, username, password):
        logger.info(f"Attempting login with username: {username}")
        logger.debug(f"Login credentials - username: {username}, password: {'*' * len(password)}")
        
        try:
            username_field = self.wait.until(
                EC.presence_of_element_located(self.USERNAME_INPUT)
            )
            username_field.clear()
            username_field.send_keys(username)
            logger.debug("Username entered successfully")
            
            password_field = self.driver.find_element(*self.PASSWORD_INPUT)
            password_field.clear()
            password_field.send_keys(password)
            logger.debug("Password entered successfully")
            
            login_button = self.driver.find_element(*self.LOGIN_BUTTON)
            login_button.click()
            logger.info("Login button clicked")
            
            from .inventory_page import InventoryPage
            return InventoryPage(self.driver)
            
        except Exception as e:
            logger.error(f"Login failed with error: {e}", exc_info=True)
            raise

    def get_error_message(self):
        try:
            error_element = self.driver.find_element(*self.ERROR_MESSAGE)
            error_text = error_element.text
            logger.debug(f"Error message found: {error_text}")
            return error_text
        except Exception:
            logger.debug("No error message present")
            return ""
