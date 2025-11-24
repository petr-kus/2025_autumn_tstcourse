from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging

logger = logging.getLogger(__name__)


class InventoryPage:
    """Page Object pro stránku s produkty SauceDemo e-shopu (inventory - katalog produktů)"""
    
    # Lokátory elementů na stránce
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def verify_user_is_logged_in(self):
        """Ověří, že uživatel je přihlášen"""
        assert "inventory" in self.driver.current_url.lower(), "Přihlášení selhalo!"
        logger.info("Uživatel je přihlášen na stránce produktů")
        return self

    def test_all_product_sorting_filters(self):
        """Vyzkouší všechny dostupné filtry pro řazení produktů (A-Z, Z-A, cena vzestupně/sestupně)"""
        logger.info("Testuji všechny filtry řazení produktů v SauceDemo")
        
        filter_dropdown = Select(self.driver.find_element(*self.FILTER_DROPDOWN))
        filter_options = filter_dropdown.options
        filter_names = [option.text for option in filter_options]
        
        for option in filter_options:
            filter_name = option.text
            filter_value = option.get_attribute("value")
            
            filter_dropdown.select_by_value(filter_value)
            
            # Ověří, že filtr je aktivní
            selected_option = filter_dropdown.first_selected_option
            assert selected_option.text == filter_name, f"Filtr '{filter_name}' nebyl správně aplikován!"
            
            # Ověří, že se zobrazují produkty
            products = self.driver.find_elements(*self.INVENTORY_ITEMS)
            assert len(products) > 0, f"Po aplikaci filtru '{filter_name}' se nezobrazují žádné produkty!"
        
        logger.info(f"Všechny filtry fungují správně: {', '.join(filter_names)}")
        return self

    def add_all_products_to_cart(self):
        """Přidá všechny produkty do košíku"""
        logger.info("Přidávám všechny produkty do košíku")
        
        add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        products_count = len(add_to_cart_buttons)
        
        assert products_count > 0, "Nebyly nalezeny žádné produkty k přidání!"
        
        for button in add_to_cart_buttons:
            button.click()
        
        # Ověří počet produktů v košíku
        cart_badge = self.driver.find_element(*self.CART_BADGE)
        cart_count = int(cart_badge.text)
        
        assert cart_count == products_count, f"V košíku je {cart_count} položek, očekáváno bylo {products_count}!"
        logger.info(f"Do košíku přidáno {products_count} produktů")
        return self

    def open_cart(self):
        """Otevře košík"""
        logger.info("Otevírám košík")
        self.driver.find_element(*self.CART_LINK).click()
        
        from .cart import CartPage
        return CartPage(self.driver)

