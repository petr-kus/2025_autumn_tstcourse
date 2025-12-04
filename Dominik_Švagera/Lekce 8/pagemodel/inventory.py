from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging

logger = logging.getLogger(__name__)


class InventoryPage:
    
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def verify_user_is_on_products_page(self):
        assert "inventory" in self.driver.current_url.lower(), "Přihlášení selhalo - nejsme na stránce produktů!"
        logger.info("Uživatel je na stránce produktů")
        return self

    def test_all_product_sorting_filters(self):
        logger.info("Testuji všechny filtry řazení produktů")
        
        filter_dropdown = Select(self.driver.find_element(*self.FILTER_DROPDOWN))
        all_filter_values = [(opt.get_attribute("value"), opt.text) for opt in filter_dropdown.options]
        
        for filter_value, filter_name in all_filter_values:
            filter_dropdown = Select(self.driver.find_element(*self.FILTER_DROPDOWN))
            filter_dropdown.select_by_value(filter_value)
            
            filter_dropdown = Select(self.driver.find_element(*self.FILTER_DROPDOWN))
            selected_filter = filter_dropdown.first_selected_option
            assert selected_filter.text == filter_name, f"Filtr '{filter_name}' není aktivní!"
            
            visible_products = self.driver.find_elements(*self.INVENTORY_ITEMS)
            assert len(visible_products) > 0, f"Filtr '{filter_name}' nezobrazuje žádné produkty!"
        
        filter_names = [name for _, name in all_filter_values]
        logger.info(f"Otestováno filtrů: {', '.join(filter_names)}")
        return self

    def add_all_products_to_cart(self):
        logger.info("Přidávám všechny produkty do košíku")
        
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        total_products = len(add_buttons)
        
        assert total_products > 0, "Nenalezeny žádné produkty k přidání!"
        
        for button in add_buttons:
            button.click()
        
        logger.info(f"Přidáno {total_products} produktů do košíku")
        return self

    def open_shopping_cart(self):
        logger.info("Otevírám nákupní košík")
        self.driver.find_element(*self.CART_ICON).click()
        
        from .cart import CartPage
        return CartPage(self.driver)


