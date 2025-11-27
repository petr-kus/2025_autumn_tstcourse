from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class InventoryPage():

    URL = "https://www.saucedemo.com/inventory.html"

    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    BADGES_CART = (By.CLASS_NAME, "shopping_cart_badge")
    IMAGE_INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item_img")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")


    def __init__(self, driver):
        self.driver = driver


    def display_products(self):
        products = self.driver.find_elements(*self.PRODUCTS)
        return products


    def choose_random_product(self, products):
        random_product = random.choice(products)
        return random_product


    def add_to_cart(self, random_product):
        product_name = random_product.find_element(*self.INVENTORY_ITEM_NAME).text
        add_button = random_product.find_element(*self.ADD_TO_CART_BUTTON)
        add_button.click()
        self.last_added_product_name = product_name
        return random_product


    def cart_count(self):
        cart_badge = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.BADGES_CART))
        if cart_badge:
            return int(cart_badge.text)
        else:
            return 0
        
        
    def go_to_cart(self):
        cart_icon = self.driver.find_element(*self.CART_ICON)
        cart_icon.click()
        

    def display_image_item(self, random_product):
        image_product = random_product.find_element(*self.IMAGE_INVENTORY_ITEM)
        return image_product.get_attribute("src")


    def display_details_item(self, random_product):
        name_product = random_product.find_element(*self.INVENTORY_ITEM_NAME)
        return name_product.text

