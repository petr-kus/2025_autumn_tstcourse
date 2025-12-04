import logging
from pagemodel import LoginPage

logger = logging.getLogger(__name__)


class TestSauceDemoStandardUser:
    
    def test_standard_user_can_login_filter_products_and_add_all_to_cart(self, browser):
        logger.info("TEST: Standardní uživatel - kompletní nákupní flow")
        
        login_page = LoginPage(browser)
        login_page.open().verify_swag_labs_is_loaded()
        
        inventory_page = login_page.login_as_standard_user()
        inventory_page.verify_user_is_on_products_page()
        
        inventory_page.test_all_product_sorting_filters()
        inventory_page.add_all_products_to_cart()
        
        cart_page = inventory_page.open_shopping_cart()
        cart_page.verify_cart_page_is_open()
        cart_page.verify_cart_contains_all_added_products()
        
        logger.info("TEST ÚSPĚŠNÝ")


class TestSauceDemoProblemUser:
    
    def test_problem_user_can_add_products_to_cart(self, browser):
        logger.info("TEST: Problémový uživatel - základní nákupní flow")
        
        login_page = LoginPage(browser)
        login_page.open().verify_swag_labs_is_loaded()
        
        inventory_page = login_page.login_as_problem_user()
        inventory_page.verify_user_is_on_products_page()
        
        inventory_page.add_all_products_to_cart()
        
        cart_page = inventory_page.open_shopping_cart()
        cart_page.verify_cart_page_is_open()
        cart_page.verify_cart_contains_all_added_products()
        
        logger.info("TEST ÚSPĚŠNÝ")
