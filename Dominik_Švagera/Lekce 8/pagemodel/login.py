from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)


class LoginPage:
    #LEKTOR: toto jsou testovaci data nemela by byt ve tride POM ale na urovni zapisu test casu
    SAUCEDEMO_URL = "https://www.saucedemo.com/"
    STANDARD_USER = "standard_user"
    PROBLEM_USER = "problem_user"
    PASSWORD = "secret_sauce"
    
    #LEKTOR: toto uz je ok...
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        logger.info(f"Otevírám SauceDemo: {self.SAUCEDEMO_URL}")
        self.driver.get(self.SAUCEDEMO_URL)
        return self

    def verify_swag_labs_is_loaded(self):
        assert "Swag Labs" in self.driver.title, f"Swag Labs se nenačetl! Titulek: {self.driver.title}"
        logger.info("Swag Labs přihlašovací stránka načtena")
        return self

    def login_as_standard_user(self):
        return self._login_with_credentials(self.STANDARD_USER, self.PASSWORD)
    
    def login_as_problem_user(self):
        return self._login_with_credentials(self.PROBLEM_USER, self.PASSWORD)
    
    def _login_with_credentials(self, username, password):
        logger.info(f"Přihlašuji uživatele: {username}")
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        
        from .inventory import InventoryPage
        return InventoryPage(self.driver)

