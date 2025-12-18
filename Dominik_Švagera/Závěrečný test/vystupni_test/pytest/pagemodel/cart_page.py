from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)


class CartPage:
    
    CART_CONTENTS = (By.ID, "cart_contents_container")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logger.debug(f"CartPage initialized with driver: {driver}")

    def verify_page_loaded(self):
        logger.debug(f"Verifying cart page loaded - current URL: {self.driver.current_url}")
        assert "cart" in self.driver.current_url.lower()
        
        self.wait.until(EC.presence_of_element_located(self.CART_CONTENTS))
        logger.info("Cart page loaded successfully")
        return self

    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        count = len(items)
        logger.debug(f"Cart contains {count} items")
        return count

    def get_product_names_in_cart(self):
        product_elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        names = [elem.text for elem in product_elements]
        logger.debug(f"Products in cart: {names}")
        logger.info(f"Cart contains {len(names)} products: {', '.join(names)}")
        return names

    def get_product_prices_in_cart(self):
        price_elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        prices = [elem.text for elem in price_elements]
        logger.debug(f"Product prices in cart: {prices}")
        return prices

    def verify_cart_not_empty(self):
        count = self.get_cart_items_count()
        assert count > 0
        logger.info(f"Cart verified to contain {count} items")
        return self

    def verify_product_in_cart(self, product_name):
        logger.debug(f"Verifying product '{product_name}' is in cart")
        product_names = self.get_product_names_in_cart()
        assert product_name in product_names
        logger.info(f"Product '{product_name}' verified in cart")
        return self

    def verify_cart_item_count(self, expected_count):
        actual_count = self.get_cart_items_count()
        assert actual_count == expected_count
        logger.info(f"Cart item count verified: {actual_count} items")
        return self

    def remove_product(self, product_index=0):
        logger.info(f"Removing product at index {product_index} from cart")
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        
        if product_index >= len(remove_buttons):
            logger.error(f"Product index {product_index} out of range")
            raise IndexError(f"Product index {product_index} out of range")
            
        remove_buttons[product_index].click()
        logger.debug(f"Product at index {product_index} removed from cart")
        return self

    def continue_shopping(self):
        logger.info("Continuing shopping - returning to inventory")
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()
        
        from .inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def proceed_to_checkout(self):
        logger.info("Proceeding to checkout")
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        logger.debug("Checkout button clicked")
        return self
