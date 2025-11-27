from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEM = (By.CSS_SELECTOR, ".cart_item")

    def items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM))

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)
