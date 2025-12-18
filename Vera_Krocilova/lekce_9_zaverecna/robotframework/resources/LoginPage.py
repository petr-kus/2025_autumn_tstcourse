from selenium.webdriver.common.by import By
from robot.api.deco import keyword
import logging
from Browser import Browser

logger = logging.getLogger(__name__)

class LoginPage:

    URL = "https://www.saucedemo.com/"
    
    LOGIN_NAME_INPUT = (By.ID, "user-name")
    LOGIN_PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self):
        self.driver = Browser.driver

    @keyword("Open Login Page")
    def open_login_page(self):
        self.driver.get(self.URL)
        
      
    @keyword("Load Login Page")  
    def load(self):
        self.driver.get(self.URL)
        logger.info("Login page loaded successfully.")
        

    @keyword ("Login User")
    def login_user(self, username, password):
        self.driver.find_element(*self.LOGIN_NAME_INPUT).send_keys(username)
        self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        logger.info("User logged in")



    