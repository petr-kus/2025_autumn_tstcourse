import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.header import Header


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    ADD_BUTTONS = (By.CSS_SELECTOR, ".inventory_item button")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)

    def is_open(self) -> bool:
        return self.is_visible(self.INVENTORY_CONTAINER, timeout=3)

    def open_cart(self):
        self.header.open_cart()

    def add_n_products(self, n: int):
        buttons = self.driver.find_elements(*self.ADD_BUTTONS)
        for btn in buttons[:n]:
            btn.click()

    def add_random_products(self, n: int):
        """
        Adds n random products to cart.
        No assertions here – UI glitches are validated in tests.
        """
        buttons = self.driver.find_elements(*self.ADD_BUTTONS)

        add_buttons = [
            btn for btn in buttons
            if btn.text.strip().lower().startswith("add")
        ]

        if len(add_buttons) < n:
            raise AssertionError(
                f"Not enough products to add: requested {n}, found {len(add_buttons)}"
            )

        chosen = random.sample(add_buttons, n)

        for btn in chosen:
            btn.click()
