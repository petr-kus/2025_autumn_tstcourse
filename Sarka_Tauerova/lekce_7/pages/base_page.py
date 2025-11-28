from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = driver._wait

    def click(self, locator):
        elm = self.wait.until(EC.element_to_be_clickable(locator))
        elm.click()

    def type(self, locator, text):
        elm = self.wait.until(EC.visibility_of_element_located(locator))
        elm.clear()
        elm.send_keys(text)

    def text(self, locator):
        elm = self.wait.until(EC.visibility_of_element_located(locator))
        return elm.text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
