from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Header(BasePage):
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.ID, "shopping_cart_container")

    def count_items_in_cart(self) -> int:
        badge = self.driver.find_elements(*self.CART_BADGE)
        if not badge:
            return 0
        return int(badge[0].text)

    def open_cart(self):
        self.click(self.CART_LINK)
