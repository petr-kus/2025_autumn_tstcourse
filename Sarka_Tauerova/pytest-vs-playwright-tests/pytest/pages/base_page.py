from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text: str):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def is_visible(self, locator, timeout: int = 0) -> bool:
        try:
            if timeout > 0:
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
            else:
                self.find(locator)
            return True
        except TimeoutException:
            return False
