from POM.LoginPage import LoginPage
from POM.InventoryPage import InventoryPage

def test_buy_backpack(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()

    assert inventory.is_in_cart()
