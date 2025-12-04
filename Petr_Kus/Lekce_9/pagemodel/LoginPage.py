
from selenium.webdriver.common.by import By
from robot.api.deco import keyword
from logging import Logger as log

class LoginPage():
    password_input = (By.ID, "password")
    login_name_input = (By.ID, "user-name")
    login_button = (By.ID, "login-button")
    
    @keyword("Open ${page} in ${browser}")
    def Open_Login_Page(self, page, browser):
        self.driver = browser
        self.load(page)

    def load(self,url):
        self.driver.get(url)

    def login_user(self, username, password):
        self.driver.find_element(*LoginPage.login_name_input).send_keys(username)
        self.driver.find_element(*LoginPage.password_input).send_keys(password)
        self.driver.find_element(*LoginPage.login_button).click()