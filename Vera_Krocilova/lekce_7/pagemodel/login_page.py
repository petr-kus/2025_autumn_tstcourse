from selenium.webdriver.common.by import By

class LoginPage:

    URL = "https://www.saucedemo.com/"
    
    LOGIN_NAME_INPUT = (By.ID, "user-name")
    LOGIN_PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver    


    def load(self, URL):
        self.driver.get(URL)

    
    def login_user(self, username, password):
        self.driver.find_element(*self.LOGIN_NAME_INPUT).send_keys(username)
        self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()




    