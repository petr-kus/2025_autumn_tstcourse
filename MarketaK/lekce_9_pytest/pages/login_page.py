from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self) -> None:
        """Otevře login stránku."""
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """Vyplní username, password a klikne na login."""
        user_el = self.driver.find_element(*self.USERNAME)
        pwd_el = self.driver.find_element(*self.PASSWORD)
        btn_el = self.driver.find_element(*self.LOGIN_BUTTON)

        user_el.clear()
        user_el.send_keys(username)

        pwd_el.clear()
        pwd_el.send_keys(password)

        btn_el.click()

    def get_error_message(self) -> str:
        """Vrátí text chybové hlášky, nebo prázdný string, pokud tam nic není."""
        elements = self.driver.find_elements(*self.ERROR_MESSAGE)
        return elements[0].text if elements else ""

    def we_are_on_page(self) -> None:
        """Jednoduchá kontrola, že jsme na login stránce."""
        assert "saucedemo.com" in self.driver.current_url
