from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)


class LoginPage:
    """Page Object pro přihlašovací stránku SauceDemo e-shopu (https://www.saucedemo.com/)"""
    
    # Lokátory elementů na stránce
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Otevře přihlašovací stránku SauceDemo e-shopu"""
        logger.info(f"Otevírám SauceDemo e-shop: {self.URL}")
        self.driver.get(self.URL)
        return self

    def verify_page_is_loaded(self):
        """Ověří, že přihlašovací stránka SauceDemo (Swag Labs) je načtena"""
        assert "Swag Labs" in self.driver.title, f"SauceDemo se nenačetl! Aktuální titulek: '{self.driver.title}'"
        logger.info("SauceDemo přihlašovací stránka načtena")
        return self

    def login_as(self, username, password):
        """Přihlásí uživatele"""
        logger.info(f"Přihlašuji uživatele: {username}")
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        

        from .inventory import InventoryPage
        return InventoryPage(self.driver)
