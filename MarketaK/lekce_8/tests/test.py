import logging
from MarketaK.lekce_8.pages.login_page import LoginPage
from MarketaK.lekce_8.pages.inventory_page import InventoryPage

def test_add_backpack_to_cart(driver):

    logging.info("STEP 1 – Open login page")
    login = LoginPage(driver)
    login.open()

    logging.info("STEP 2 – Login as standard_user")
    login.login("standard_user", "secret_sauce")

    logging.info("STEP 3 – Add backpack to cart")
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()

    assert inventory.is_in_cart(), " Backpack was NOT added to cart!"

    logging.info("✔ Backpack successfully added to cart")
