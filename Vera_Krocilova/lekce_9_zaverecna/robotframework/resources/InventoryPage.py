from selenium.webdriver.common.by import By
import random
from robot.api.deco import keyword
from Browser import Browser
import logging

logger = logging.getLogger(__name__)



class InventoryPage:

    URL = "https://www.saucedemo.com/inventory.html"

    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".pricebar button")
    BADGES_CART = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".inventory_item_img img")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")


    def __init__(self):
        self.driver = Browser.driver

    @keyword("Set Driver")
    def set_driver(self, driver):
        self.driver = driver

    @keyword("Use Browser")
    def use_browser(self, browser):
        self.driver = browser.get_driver()

    @keyword("Go Back")
    def go_back(self):
        self.driver.back()

    @keyword ("Display Products")
    def display_products(self):
        products = self.driver.find_elements(*self.PRODUCTS)
        logger.info(f"Found {len(products)} products on inventory page.")
        return products

    @keyword ("Select Random Product")
    def choose_random_product(self, products):
        random_product = random.choice(products)   
        logger.info(f"Random product '{random_product}' selected successfully.")  
        return random_product

    @keyword ("Add Product To Cart")
    def add_to_cart(self, random_product):
        name_product = random_product.find_element(*self.PRODUCT_NAME).text
        add_button = random_product.find_element(*self.ADD_TO_CART_BUTTON)
        add_button.click()
        logger.info(f"Random product '{name_product}' added to cart.")
        return name_product
        
    @keyword ("Get Cart Items Count")
    def cart_count(self):
        cart_badge = self.driver.find_element(*self.BADGES_CART)
        if cart_badge:
            return int(cart_badge.text)
        else:
            return 0
        
    @keyword ("Go To Cart")    
    def go_to_cart(self):
        cart_icon = self.driver.find_element(*self.CART_ICON)
        cart_icon.click()
        logger.info("Navigated to cart page.")

    @keyword("Get Product Name Text")
    def get_product_name_text(self, product):
        name_element = product.find_element(*self.PRODUCT_NAME)
        return name_element

        
    @keyword("Click Product Image") 
    def click_product_image(self, product):
        image = product.find_element(*self.PRODUCT_IMAGE)
        src = image.get_attribute("src")
        image.click()
        logger.info(f"Product image '{image}' displayed successfully.")
        return src

    @keyword("Get Product Detail Image Src")
    def get_detail_image_src(self):
        detail_image = self.driver.find_element(By.CLASS_NAME, "inventory_details_img")
        return detail_image.get_attribute("src")

    @keyword("Click Product Name")
    def click_product_name(self, random_product):
        name_element = random_product.find_element(*self.PRODUCT_NAME)
        name_text = name_element.text
        name_element.click()
        logger.info(f"Product details '{name_text}' displayed successfully.")
        return name_text
    
    @keyword("Get Product Name Text")
    def get_product_name_text(self, random_product):
        return random_product.find_element(*self.PRODUCT_NAME).text
   
    @keyword("Get Product Detail Name")
    def get_detail_name(self):
        detail_name = self.driver.find_element(By.CLASS_NAME, "inventory_details_name")
        return detail_name.text
        
        

