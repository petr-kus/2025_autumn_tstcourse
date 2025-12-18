import pytest
import logging
from pagemodel import LoginPage, InventoryPage, CartPage

logger = logging.getLogger(__name__)

APP_URL = "https://www.saucedemo.com/"
STANDARD_USER = "standard_user"
PROBLEM_USER = "problem_user"
PASSWORD = "secret_sauce"


class TestLoginAndCart:
    
    def test_successful_login_and_cart_operations(self, browser):
        logger.info("Starting test: successful_login_and_cart_operations")
        logger.debug(f"Test data - URL: {APP_URL}, User: {STANDARD_USER}")
        
        login_page = LoginPage(browser)
        login_page.open(APP_URL).verify_page_loaded()
        
        inventory_page = login_page.login(STANDARD_USER, PASSWORD)
        inventory_page.verify_page_loaded()
        
        product_count = inventory_page.get_product_count()
        logger.info(f"Found {product_count} products on inventory page")
        assert product_count > 0
        
        product_names = inventory_page.get_product_names()
        logger.info(f"Available products: {product_names}")
        
        inventory_page.add_all_products_to_cart()
        
        cart_badge_count = inventory_page.get_cart_badge_count()
        logger.info(f"Cart badge shows: {cart_badge_count} items")
        if cart_badge_count > 0:
            assert cart_badge_count == product_count
        else:
            logger.warning("Cart badge not displayed - skipping badge verification")
        
        cart_page = inventory_page.open_cart()
        cart_page.verify_page_loaded()
        
        cart_page.verify_cart_not_empty()
        cart_page.verify_cart_item_count(product_count)
        
        products_in_cart = cart_page.get_product_names_in_cart()
        logger.info(f"Products in cart: {products_in_cart}")
        
        for product_name in product_names:
            cart_page.verify_product_in_cart(product_name)
        
        logger.info("Test completed successfully")


class TestProductFiltering:
    
    def test_filter_products_and_add_to_cart(self, browser):
        logger.info("Starting test: filter_products_and_add_to_cart")
        logger.debug(f"Test data - URL: {APP_URL}, User: {STANDARD_USER}")
        
        login_page = LoginPage(browser)
        inventory_page = login_page.open(APP_URL).verify_page_loaded() \
            .login(STANDARD_USER, PASSWORD)
        inventory_page.verify_page_loaded()
        
        logger.info("Testing product filter: Price (high to low)")
        inventory_page.apply_filter("hilo")
        inventory_page.verify_filter_applied("Price (high to low)")
        
        products_after_filter = inventory_page.get_product_names()
        logger.info(f"Products after filtering: {products_after_filter}")
        
        num_products_to_add = min(3, len(products_after_filter))
        logger.info(f"Adding {num_products_to_add} products to cart")
        
        for i in range(num_products_to_add):
            inventory_page.add_product_to_cart(i)
        
        cart_badge = inventory_page.get_cart_badge_count()
        assert cart_badge == num_products_to_add
        
        cart_page = inventory_page.open_cart()
        cart_page.verify_page_loaded()
        cart_page.verify_cart_item_count(num_products_to_add)
        
        logger.info("Test completed successfully")


class TestProblemUser:
    
    def test_problem_user_login_and_cart(self, browser):
        logger.info("Starting test: problem_user_login_and_cart")
        logger.debug(f"Test data - URL: {APP_URL}, User: {PROBLEM_USER}")
        logger.warning("Testing with problem_user - bugs may be encountered")
        
        try:
            login_page = LoginPage(browser)
            inventory_page = login_page.open(APP_URL).verify_page_loaded() \
                .login(PROBLEM_USER, PASSWORD)
            inventory_page.verify_page_loaded()
            
            inventory_page.add_all_products_to_cart()
            
            cart_page = inventory_page.open_cart()
            cart_page.verify_page_loaded()
            cart_page.verify_cart_not_empty()
            
            products_in_cart = cart_page.get_product_names_in_cart()
            logger.info(f"Problem user cart contains: {products_in_cart}")
            
            logger.info("Test completed - problem_user behaved correctly")
            
        except AssertionError as e:
            logger.error(f"Bug detected with problem_user: {e}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Unexpected error with problem_user: {e}", exc_info=True)
            raise
