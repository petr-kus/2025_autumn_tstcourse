from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import logging
import os



logger = logging.getLogger(__name__)


class InventoryPage():


    URL = "https://www.saucedemo.com/inventory.html"

    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".pricebar button")
    BADGES_CART = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".inventory_item_img img")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")


    def take_screenshot(self, name="screenshot.png"):
        os.makedirs("screenshots", exist_ok=True)
        filepath = os.path.join("screenshots", f"{name}.png")
        self.driver.save_screenshot(filepath)
        
    

    def __init__(self, driver):
        self.driver = driver




    def display_products(self):
        products = self.driver.find_elements(*self.PRODUCTS)
        logger.info(f"Found {len(products)} products on inventory page.")
        return products

    def choose_random_product(self, products):
        random_product = random.choice(products)     
        logger.info(f"Random product '{random_product}' selected successfully.")
        return random_product

    def add_to_cart(self, random_product):
        name_product = random_product.find_element(*self.PRODUCT_NAME).text
        add_button = random_product.find_element(*self.ADD_TO_CART_BUTTON)
        add_button.click()
        logger.info(f"Random product '{name_product}' added to cart.")
        return name_product
        

    def cart_count(self):
        cart_badge = self.driver.find_element(*self.BADGES_CART)
        if cart_badge:
            return int(cart_badge.text)
        else:
            return 0
        
        
        
    def go_to_cart(self):
        cart_icon = self.driver.find_element(*self.CART_ICON)
        cart_icon.click()
        logger.info("Navigated to cart page.")
        

    def click_product_image(self, random_product):
        product_image = random_product.find_element(*self.PRODUCT_IMAGE)
        image_src = product_image.get_attribute("src")
        product_image.click()
        logger.info(f"Product image '{product_image}' displayed successfully.")
        return image_src


    def get_detail_image_src(self):
        detail_image = self.driver.find_element(By.CLASS_NAME, "inventory_details_img")
        return detail_image.get_attribute("src")


    def click_product_name(self, random_product):
        name_product = random_product.find_element(*self.PRODUCT_NAME)
        name_product_text = name_product.text
        name_product.click()
        logger.info(f"Product details '{name_product}' displayed successfully.")
        return name_product_text
   
    
    def get_detail_name(self):
        detail_name = self.driver.find_element(By.CLASS_NAME, "inventory_details_name")
        return detail_name.text
        
        

