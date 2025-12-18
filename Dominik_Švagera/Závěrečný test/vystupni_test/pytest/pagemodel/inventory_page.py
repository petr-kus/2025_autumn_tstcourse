from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import logging

logger = logging.getLogger(__name__)


class InventoryPage:
    
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logger.debug(f"InventoryPage initialized with driver: {driver}")

    def verify_page_loaded(self):
        logger.debug(f"Verifying inventory page loaded - current URL: {self.driver.current_url}")
        assert "inventory" in self.driver.current_url.lower()
        
        self.wait.until(EC.presence_of_element_located(self.INVENTORY_CONTAINER))
        logger.info("Inventory page loaded successfully")
        return self

    def get_product_count(self):
        products = self.driver.find_elements(*self.INVENTORY_ITEMS)
        count = len(products)
        logger.debug(f"Found {count} products on inventory page")
        return count

    def get_product_names(self):
        product_elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        names = [elem.text for elem in product_elements]
        logger.debug(f"Product names: {names}")
        return names

    def apply_filter(self, filter_value):
        logger.info(f"Applying filter: {filter_value}")
        filter_dropdown = Select(self.driver.find_element(*self.FILTER_DROPDOWN))
        filter_dropdown.select_by_value(filter_value)
        logger.debug(f"Filter '{filter_value}' applied successfully")
        return self

    def verify_filter_applied(self, expected_filter_text):
        filter_dropdown = Select(self.driver.find_element(*self.FILTER_DROPDOWN))
        selected_option = filter_dropdown.first_selected_option.text
        logger.debug(f"Current filter: {selected_option}")
        
        assert selected_option == expected_filter_text
        logger.info(f"Filter '{expected_filter_text}' verified successfully")
        return self

    def add_product_to_cart(self, product_index=0):
        logger.info(f"Adding product at index {product_index} to cart")
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        
        if product_index >= len(add_buttons):
            logger.error(f"Product index {product_index} out of range")
            raise IndexError(f"Product index {product_index} out of range")
            
        add_buttons[product_index].click()
        logger.debug(f"Product at index {product_index} added to cart")
        return self

    def add_all_products_to_cart(self):
        logger.info("Adding all products to cart")
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        total_products = len(add_buttons)
        
        for idx, button in enumerate(add_buttons):
            button.click()
            logger.debug(f"Added product {idx + 1}/{total_products} to cart")
        
        logger.info(f"Successfully added {total_products} products to cart")
        return self

    def get_cart_badge_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            count = int(badge.text)
            logger.debug(f"Cart badge shows: {count}")
            return count
        except Exception:
            logger.debug("Cart badge not present")
            return 0

    def open_cart(self):
        logger.info("Opening shopping cart")
        self.driver.find_element(*self.CART_ICON).click()
        
        from .cart_page import CartPage
        return CartPage(self.driver)
