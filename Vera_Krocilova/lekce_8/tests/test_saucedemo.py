from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import logging
import pytest

# Testovací data
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.mark.parametrize("URL, USERNAME, PASSWORD", [(URL,USERNAME,PASSWORD)] )
def test_login_page(browser, URL, USERNAME, PASSWORD):
  
    login_page = LoginPage(browser)

    login_page.load(URL)
    assert browser.current_url == URL, f"Incorrect page loaded. Current url: '{browser.current_url}'"
    logging.info("Login page loaded successfully.")

    login_page.login_user(USERNAME, PASSWORD)
    assert "inventory" in browser.current_url.lower(), "Login failed!"
    logging.info("Login successful.")

  
def test_add_to_cart(browser):
    
    inventory_page = InventoryPage(browser)
        
    get_all_products = inventory_page.display_products()
    assert len(get_all_products) > 0, "No products found on inventory page!"
    logging.info(f"Found {len(get_all_products)} products on inventory page.")

    selected_product = inventory_page.choose_random_product(get_all_products)
    assert selected_product is not None, "Failed to select a random product."
    logging.info(f"Random product '{selected_product}' selected successfully.")

    product_in_cart = inventory_page.add_to_cart(selected_product)
    logging.info(f"Random product '{product_in_cart}' added to cart.")
       
    cart_count = inventory_page.cart_count()
    assert cart_count == 1, f"Cart count expected to be 1 but got {cart_count}."
    logging.info("Cart count verified successfully.")
        
    inventory_page.go_to_cart()
    assert "cart" in browser.current_url.lower(), "Failed to navigate to cart page."
    logging.info("Navigated to cart page.")
    #LEKTOR: zde bych obecne doporucil majoritu toho logovani presunout do metod v page obejct modelu

    inventory_page.driver.back()
         
       
def test_view_product_image(logged_in_inventory_page, any_product):
   
    inventory_page = logged_in_inventory_page
    product = any_product
    product_name = product.text
                
    expected_image_src = inventory_page.click_product_image(product)
    actual_image_src = inventory_page.get_detail_image_src()
    assert expected_image_src is not None, "Failed to get selected product image src."
    assert expected_image_src == actual_image_src, (f"Expected image src {expected_image_src} but got {actual_image_src}.") 
    logging.info(f"Product image '{product_name}' displayed successfully.")

    inventory_page.driver.back()
       
        
def test_click_product_name(logged_in_inventory_page, any_product):
    
    inventory_page = logged_in_inventory_page
    product = any_product
    product_name = product.text
        
    expected_name = inventory_page.click_product_name(product)
    actual_name = inventory_page.get_detail_name()
    assert expected_name == actual_name, (f"Expected product {expected_name} but got {actual_name}.")
    logging.info(f"Product details '{product_name}' displayed successfully.")

        




