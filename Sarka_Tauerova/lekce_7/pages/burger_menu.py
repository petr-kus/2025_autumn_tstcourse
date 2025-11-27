from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BurgerMenu(BasePage):
    OPEN_BTN = (By.ID, "react-burger-menu-btn")
    CLOSE_BTN = (By.ID, "react-burger-cross-btn")
    LOGOUT = (By.XPATH, "//a[text()='Logout']")
    ALL_ITEMS = (By.XPATH, "//a[text()='All Items']")
    RESET_APP = (By.XPATH, "//a[text()='Reset App State']")

    def open(self):
        self.click(self.OPEN_BTN)
        self.is_visible(self.CLOSE_BTN)

    def logout(self):
        self.open()
        self.click(self.LOGOUT)

    def go_to_all_items(self):
        self.open()
        self.click(self.ALL_ITEMS)

    def reset_app_state(self):
        self.open()
        self.click(self.RESET_APP)
