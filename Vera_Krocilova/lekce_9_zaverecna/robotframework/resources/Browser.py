from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from robot.api.deco import keyword
import logging
import os


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='test.log')

class Browser:

    driver = None


    @keyword("Open Browser")
    def open_browser(self):
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("--guest")
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
        options.add_experimental_option("prefs", prefs)

        Browser.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        Browser.driver.implicitly_wait(5)
        logging.info("Browser initialized and maximized.")   


    @keyword("Get Driver")
    def get_driver(self):
        return Browser.driver

    @keyword("Close Browser")
    def close_browser(self):
        if Browser.driver:
            Browser.driver.quit()


    @keyword("Take Screenshot")
    def take_screenshot(self, name="screenshot.png"):
        if not Browser.driver:
            logging.error("Driver is not initialized. Cannot take screenshot.")
            return
        os.makedirs("screenshots", exist_ok=True)
        filepath = os.path.join("screenshots", name)
        Browser.driver.save_screenshot(filepath)
        logging.info(f"Screenshot saved to {filepath}")