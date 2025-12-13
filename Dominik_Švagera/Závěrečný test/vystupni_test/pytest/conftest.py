import pytest
import logging
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

LOGS_DIR = Path(__file__).parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

log_filename = LOGS_DIR / f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def pytest_configure(config):
    logger.info("=" * 80)
    logger.info("TEST SUITE STARTED")
    logger.info(f"Log file: {log_filename}")
    logger.info("=" * 80)


def pytest_unconfigure(config):
    logger.info("=" * 80)
    logger.info("TEST SUITE COMPLETED")
    logger.info("=" * 80)


@pytest.fixture(scope="function")
def browser():
    logger.info("Setting up browser")
    logger.debug("Initializing Chrome WebDriver with ChromeDriverManager")
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        logger.info("Browser started successfully")
        logger.debug(f"Browser session ID: {driver.session_id}")
        
        yield driver
        
    except Exception as e:
        logger.error(f"Failed to start browser: {e}", exc_info=True)
        raise
        
    finally:
        logger.info("Tearing down browser")
        try:
            driver.quit()
            logger.info("Browser closed successfully")
        except Exception as e:
            logger.error(f"Error closing browser: {e}", exc_info=True)


@pytest.fixture(scope="function", autouse=True)
def log_test_info(request):
    test_name = request.node.name
    logger.info("-" * 80)
    logger.info(f"TEST STARTED: {test_name}")
    logger.info("-" * 80)
    
    yield
    
    logger.info("-" * 80)
    logger.info(f"TEST FINISHED: {test_name}")
    logger.info("-" * 80)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        test_name = item.name
        if report.passed:
            logger.info(f"TEST PASSED: {test_name}")
        elif report.failed:
            logger.error(f"TEST FAILED: {test_name}")
            logger.error(f"Failure reason: {report.longreprtext}")
        elif report.skipped:
            logger.warning(f"TEST SKIPPED: {test_name}")
