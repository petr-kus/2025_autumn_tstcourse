from selenium.webdriver.common.by import By
from robot.api.deco import keyword


class InventoryPage:
    title = (By.CLASS_NAME, "title")
    backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    inventory_item_images = (By.CSS_SELECTOR, ".inventory_item_img img")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    @keyword("Inventory page should be open")
    def inventory_page_should_be_open(self, browser):
        title_el = browser.find_element(*self.title)
        assert title_el.text == "Products"

    @keyword("Add backpack to cart in ${browser}")
    def add_backpack_to_cart(self, browser):
        browser.find_element(*self.backpack_add_button).click()

    @keyword("Cart badge should show 1 in ${browser}")
    def cart_badge_should_show_1(self, browser):
        badge_text = browser.find_element(*self.cart_badge).text
        assert badge_text == "1"

    @keyword("All inventory images should be visible in ${browser}")
    def all_inventory_images_should_be_visible(self, browser):
        images = browser.find_elements(*self.inventory_item_images)
        assert images, "Nebyly nalezeny žádné obrázky produktů"
        for img in images:
            assert img.is_displayed(), "Některé obrázky nejsou vidět"

    @keyword("Logout via menu in ${browser}")
    def logout_via_menu(self, browser):
        browser.find_element(*self.menu_button).click()
        browser.find_element(*self.logout_link).click()
