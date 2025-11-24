from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)


class CartPage:
    """Page Object pro nákupní košík SauceDemo e-shopu"""
    
    # Lokátory elementů na stránce
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def verify_cart_page_is_open(self):
        """Ověří, že je otevřena stránka košíku"""
        assert "cart" in self.driver.current_url.lower(), "Nejsme na stránce košíku!"
        logger.info("Stránka košíku je otevřena")
        return self

    def verify_cart_contains_products(self):
        """Ověří, že nákupní košík obsahuje produkty a vypíše jejich názvy"""
        cart_items = self.driver.find_elements(*self.CART_ITEMS)
        items_count = len(cart_items)
        
        assert items_count > 0, "Nákupní košík v SauceDemo je prázdný, ale měl by obsahovat produkty!"
        
        product_names = []
        for item in cart_items:
            name = item.find_element(*self.ITEM_NAME).text
            product_names.append(name)
        
        logger.info(f"Košík obsahuje {items_count} produktů: {', '.join(product_names)}")
        return self
