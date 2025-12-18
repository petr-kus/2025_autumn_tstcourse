from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def items_count(self) -> int:
        return len(self.find_elements(self.ITEM))

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
