from selenium.common.exceptions import TimeoutException

from conftest import USERS
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_problem_user_checkout_fails(driver):
    """
    problem_user is not able to successfully finish checkout.
    The test expects checkout to fail before completion.
    """

    username, password = next(
        (u, p) for (u, p) in USERS if u == "problem_user"
    )

    login = LoginPage(driver)
    login.login(username, password)

    inventory = InventoryPage(driver)
    assert inventory.is_open()

    inventory.add_n_products(1)
    inventory.open_cart()

    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_and_continue("Jan", "Novak", "12345")

    try:
        checkout.finish()
    except TimeoutException:
        return

    assert not checkout.is_complete(), (
        "problem_user was able to complete checkout — failure was expected"
    )
