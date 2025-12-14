from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_CONTAINER = (By.CSS_SELECTOR, ".error-message-container")

    def open(self):
        self.open_url(self.URL)

    def login(self, username: str, password: str):
        self.open()
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def error_visible(self) -> bool:
        return self.is_visible(self.ERROR_CONTAINER, timeout=1)
