from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_and_continue(self, first, last, zip_code):
        self.type(self.FIRST, first)
        self.type(self.LAST, last)
        self.type(self.ZIP, zip_code)
        self.click(self.CONTINUE)

    def finish(self):
        self.click(self.FINISH)

    def is_complete(self):
        return self.is_visible(self.COMPLETE_HEADER)
