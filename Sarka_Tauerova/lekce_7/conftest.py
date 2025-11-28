import logging
import pytest
import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(filename="my_log.log", level=logging.DEBUG,
                    format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

TEST_PAGE = "https://www.saucedemo.com/"
EXPLICIT_WAIT = 8

@pytest.fixture(scope="function")
def driver():
    user_data_dir = tempfile.mkdtemp(prefix="selenium-profile-")
    log.debug("Temp profile: %s", user_data_dir)

    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--incognito")
    opts.add_argument("--no-first-run")
    opts.add_argument("--no-default-browser-check")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.exit_type": "None",
        "profile.exited_cleanly": True,
    }
    opts.add_experimental_option("prefs", prefs)
    opts.add_argument(f"--user-data-dir={user_data_dir}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)

    driver._wait = WebDriverWait(driver, EXPLICIT_WAIT)

    driver.get(TEST_PAGE)

    yield driver

    try:
        driver.quit()
    finally:
        shutil.rmtree(user_data_dir, ignore_errors=True)
        log.debug("Removed temp profile: %s", user_data_dir)
