from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def Browser_is_running():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver