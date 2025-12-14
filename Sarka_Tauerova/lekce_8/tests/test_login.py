from conftest import USERS
from pages.login_page import LoginPage


def test_all_users_can_login_except_locked_out(driver):
    """
    All users except locked_out_user should be able to log in successfully.
    locked_out_user must see an error message.
    """

    for username, password in USERS:
        login = LoginPage(driver)
        page = login.login(username, password)

        if username == "locked_out_user":
            assert login.error_visible(), "Locked out user should see login error"
        else:
            assert page.is_open(), f"User {username} was not able to log in"
