import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def logger():
    logger = logging.getLogger("saucedemo_tests")
    logger.setLevel(logging.INFO)
    return logger


@pytest.fixture
def driver(logger):
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    logger.info("Starting browser")
    yield driver
    logger.info("Quitting browser")
    driver.quit()
