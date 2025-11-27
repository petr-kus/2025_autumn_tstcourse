import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password,should_login",
    [
        ("standard_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False),
    ]
)
def test_login(driver, username, password, should_login):
    login = LoginPage(driver)
    login.login(username, password)
    if should_login:
        from pages.inventory_page import InventoryPage
        inv = InventoryPage(driver)
        assert inv.is_open()
    else:
        assert login.error_visible()
