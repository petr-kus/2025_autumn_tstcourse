from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from robot.api.deco import keyword


@keyword("Browser is running")
def browser_is_running():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver
