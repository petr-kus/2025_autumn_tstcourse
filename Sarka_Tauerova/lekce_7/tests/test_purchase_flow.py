import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_add_items_and_checkout(driver, username, password):
    login = LoginPage(driver)
    login.login(username, password)

    inventory = InventoryPage(driver)
    assert inventory.is_open()

    add_count = 3
    inventory.add_n_products(add_count)
    assert inventory.cart_count() == add_count

    inventory.open_cart()

    cart = CartPage(driver)
    assert cart.items_count() == add_count

    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_and_continue("Jan", "Novak", "12345")
    checkout.finish()
    assert checkout.is_complete()
