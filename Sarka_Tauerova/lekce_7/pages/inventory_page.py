import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def is_open(self):
        return self.is_visible(self.INVENTORY_CONTAINER)

    def cart_count(self):
        try:
            txt = self.driver.find_element(*self.CART_BADGE).text.strip()
            return int(txt) if txt else 0
        except:
            return 0

    def add_n_products(self, n: int):
        added = 0
        attempts = 0
        while added < n and attempts < 40:
            attempts += 1
            items = self.driver.find_elements(*self.ITEMS)
            if not items:
                time.sleep(0.1)
                continue
            for card in items:
                try:
                    btn = card.find_element(By.TAG_NAME, "button")
                    if btn.text.strip() != "Add to cart":
                        continue
                    self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
                    btn.click()
                    WebDriverWait(self.driver, 2).until(lambda d: self.cart_count() >= added + 1)
                    added += 1
                    if added >= n:
                        break
                except:
                    continue
        if added != n:
            raise AssertionError(f"Expected to add {n} items, but only added {added} (attempts={attempts}).")

    def open_cart(self):
        self.click(self.CART_LINK)
