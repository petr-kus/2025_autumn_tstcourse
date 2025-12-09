import time
import pytest
import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

BASE_URL = "https://www.saucedemo.com/"

STANDARD_USER = "standard_user"
PROBLEM_USER = "problem_user"
PASSWORD = "secret_sauce"



@pytest.fixture
def username_standard():
    return STANDARD_USER


@pytest.fixture
def username_problem():
    return PROBLEM_USER


@pytest.fixture
def password():
    return PASSWORD


def slowdown(seconds: float = 1.5):
    time.sleep(seconds)




@allure.feature("Login")
@allure.story("Valid login with standard_user")
def test_login_the_user(driver, logger, username_standard, password):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    logger.info("Opening login page")
    login_page.open()          
    slowdown()

    logger.info("Logging in as standard_user")
    login_page.login(username_standard, password)
    slowdown()

    title = inventory_page.get_title_text()
    logger.info(f"Inventory page title: {title}")
    inventory_page.we_are_on_page()
    assert title == "Products"


@allure.feature("Login")
@allure.story("Problem_user – expected fail")
@pytest.mark.xfail(reason="Zadání: login problem_user má test neprojde")
def test_login_problem_user(driver, logger, username_problem, password):
    login_page = LoginPage(driver)

    logger.info("Opening login page for problem_user")
    login_page.open()
    slowdown()

    logger.info("Logging in as problem_user")
    login_page.login(username_problem, password)
    slowdown()

  
    error_text = login_page.get_error_message()
    logger.info(f"Error message for problem_user: {error_text}")
    assert "Epic sadface" in error_text


@allure.feature("Cart")
@allure.story("Cart badge behavior – add and keep item")
def test_cart_badge_behavior(driver, logger, username_standard, password):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(username_standard, password)
    slowdown()

    logger.info("Adding backpack to cart")
    inventory_page.add_backpack_to_cart()
    slowdown()

    cart_count = inventory_page.get_cart_count()
    logger.info(f"Cart count after add: {cart_count}")
    assert cart_count == 1




@allure.feature("UI")
@allure.story("All product images are visible")
def test_all_product_images_visible(driver, logger, username_standard, password):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(username_standard, password)
    slowdown()

    logger.info("Checking visibility of all inventory item images")
    all_visible = inventory_page.all_item_images_displayed()
    logger.info(f"All images visible: {all_visible}")
    assert all_visible is True


@allure.feature("Logout")
@allure.story("Logout from inventory page")
def test_logout_a_user(driver, logger, username_standard, password):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(username_standard, password)
    slowdown()

    logger.info("Performing logout from inventory page")
    inventory_page.logout()
    slowdown()

    logger.info(f"Current URL after logout: {driver.current_url}")
    login_page.we_are_on_page()
    assert "https://www.saucedemo.com/" in driver.current_url
