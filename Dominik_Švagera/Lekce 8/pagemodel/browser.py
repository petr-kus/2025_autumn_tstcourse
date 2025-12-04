from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging

logger = logging.getLogger(__name__)


class Browser:
    """Page Object pro správu prohlížeče"""
    
    @staticmethod
    def start():
        """Spustí prohlížeč"""
        logger.info("Spouštím prohlížeč")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return driver
    
    @staticmethod
    def stop(driver):
        """Zastaví prohlížeč"""
        logger.info("Zastavuji prohlížeč")
        driver.quit()
