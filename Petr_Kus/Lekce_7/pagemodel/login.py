
from selenium.webdriver.common.by import By

class LoginPage:
    password_input = (By.ID, "password")
    login_name_input = (By.ID, "user-name")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def load(self,url):
        self.driver.get(url)

    def login_user(self, username, password):
        self.driver.find_element(*LoginPage.login_name_input).send_keys(username)
        self.driver.find_element(*LoginPage.password_input).send_keys(password)
        self.driver.find_element(*LoginPage.login_button).click()