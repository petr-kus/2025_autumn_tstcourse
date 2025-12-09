from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    INVENTORY_ITEM_IMAGES = (By.CSS_SELECTOR, ".inventory_item_img img")

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_title_text(self) -> str:
        return self.driver.find_element(*self.TITLE).text

    def we_are_on_page(self) -> None:
        assert self.get_title_text() == "Products"

    def add_backpack_to_cart(self) -> None:
        self.driver.find_element(*self.BACKPACK_ADD_BUTTON).click()

    def get_cart_count(self) -> int:
        elements = self.driver.find_elements(*self.CART_BADGE)
        if not elements:
            return 0
        return int(elements[0].text)

    def open_cart(self) -> None:
        self.driver.find_element(*self.CART_LINK).click()

    def all_item_images_displayed(self) -> bool:
        images = self.driver.find_elements(*self.INVENTORY_ITEM_IMAGES)
        if not images:
            return False
        return all(img.is_displayed() for img in images)

    def logout(self) -> None:
        self.driver.find_element(*self.MENU_BUTTON).click()
        self.driver.find_element(*self.LOGOUT_LINK).click()

