class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def is_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()
