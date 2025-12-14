import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


USERS = [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
]

positive_users = [
    user for user in USERS
    if user[0] != "locked_out_user"
]


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)
    driver.wait = wait
    driver._wait = wait

    yield driver

    driver.quit()


@pytest.fixture
def user_is_logged(request, driver):
    from pages.login_page import LoginPage
    from pages.inventory_page import InventoryPage

    username, password = request.param

    login = LoginPage(driver)
    page = login.login(username, password)

    if isinstance(page, InventoryPage):
        return page

    return page
