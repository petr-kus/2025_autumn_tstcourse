from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)


class CartPage:
    
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def verify_cart_page_is_open(self):
        assert "cart" in self.driver.current_url.lower(), "Nejsme na stránce košíku!"
        logger.info("Stránka nákupního košíku je otevřena")
        return self

    def verify_cart_contains_all_added_products(self):
        items_in_cart = self.driver.find_elements(*self.CART_ITEMS)
        total_items = len(items_in_cart)
        
        assert total_items > 0, "Košík je prázdný!"
        
        product_names = [item.find_element(*self.PRODUCT_NAME).text for item in items_in_cart]
        
        logger.info(f"Košík obsahuje {total_items} produktů: {', '.join(product_names)}")
        return self

