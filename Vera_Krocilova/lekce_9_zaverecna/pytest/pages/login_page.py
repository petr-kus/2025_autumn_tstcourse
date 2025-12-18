from selenium.webdriver.common.by import By
import logging
import os


logger = logging.getLogger(__name__)

class LoginPage:

    URL = "https://www.saucedemo.com/"
    
    LOGIN_NAME_INPUT = (By.ID, "user-name")
    LOGIN_PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")


    def take_screenshot(self, name="screenshot.png"):
        os.makedirs("screenshots", exist_ok=True)
        filepath = os.path.join("screenshots", f"{name}.png")
        self.driver.save_screenshot(filepath)
        

    def __init__(self, driver):
        self.driver = driver    


    def load(self, URL):
        self.driver.get(URL)
        logger.info("Login page loaded successfully.")

    
    def login_user(self, username, password):
        self.driver.find_element(*self.LOGIN_NAME_INPUT).send_keys(username)
        self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        logger.info("Logging in as user '%s'", username)
        logger.error("Login failed")

        


    