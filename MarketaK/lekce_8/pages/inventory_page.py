from selenium.webdriver.common.by import By
from MarketaK.lekce_8.pages.base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD)

    def is_in_cart(self):
        return self.is_visible(self.CART_BADGE)

