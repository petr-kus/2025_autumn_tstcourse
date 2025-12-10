from selenium.webdriver.common.by import By
from robot.api.deco import keyword


class LoginPage:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")

    @keyword("Open ${page} in ${browser}")
    def open_login_page(self, page, browser):
        browser.get(page)

    @keyword("Login User")
    def login_user(self, browser, username, password):
        user_el = browser.find_element(*self.username_input)
        pwd_el = browser.find_element(*self.password_input)
        btn_el = browser.find_element(*self.login_button)

        user_el.clear()
        user_el.send_keys(username)

        pwd_el.clear()
        pwd_el.send_keys(password)

        btn_el.click()

    @keyword("Login page should be open")
    def login_page_should_be_open(self, browser):
        assert "saucedemo.com" in browser.current_url

