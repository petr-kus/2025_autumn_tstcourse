from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.ID, "shopping_cart_container")

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK)
        self.click(self.CART)

    def is_in_cart(self):
        return "cart" in self.driver.current_url
