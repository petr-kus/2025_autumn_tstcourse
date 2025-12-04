import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging

logger = logging.getLogger(__name__)


@pytest.fixture
def browser():
    logger.info("Spouštím prohlížeč")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    logger.info("Zastavuji prohlížeč")
    driver.quit()
