class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(self.url)

    def login(self, username, password):
        username_field = self.driver.find_element("id", "user-name")
        password_field = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("id", "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()