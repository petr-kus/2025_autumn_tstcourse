from robot.api import logger
from robot.api.deco import keyword
from datetime import datetime
from pathlib import Path
import logging


class WebAppLibrary:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = '1.0'
    
    def __init__(self):
        self._setup_logging()
        self.log_info("WebAppLibrary initialized")
    
    def _setup_logging(self):
        logs_dir = Path(__file__).parent.parent / "logs"
        logs_dir.mkdir(exist_ok=True)
        
        log_filename = logs_dir / f"robot_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        self.logger = logging.getLogger('WebAppLibrary')
        self.logger.setLevel(logging.DEBUG)
        
        file_handler = logging.FileHandler(log_filename, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
        logger.info(f"Python logging configured - log file: {log_filename}")
    
    @keyword("Log Debug Message")
    def log_debug(self, message):
        logger.debug(message)
        self.logger.debug(message)
    
    @keyword("Log Info Message")
    def log_info(self, message):
        logger.info(message)
        self.logger.info(message)
    
    @keyword("Log Warning Message")
    def log_warning(self, message):
        logger.warn(message)
        self.logger.warning(message)
    
    @keyword("Log Error Message")
    def log_error(self, message):
        logger.error(message)
        self.logger.error(message)
    
    @keyword("Log Test Step")
    def log_test_step(self, step_number, step_description):
        message = f"STEP {step_number}: {step_description}"
        logger.info(message)
        self.logger.info(message)
    
    @keyword("Log Test Data")
    def log_test_data(self, data_name, data_value):
        message = f"Test Data - {data_name}: {data_value}"
        logger.debug(message)
        self.logger.debug(message)
    
    @keyword("Log Assertion")
    def log_assertion(self, assertion_description, actual_value, expected_value):
        message = f"Assertion - {assertion_description}: Expected='{expected_value}', Actual='{actual_value}'"
        logger.info(message)
        self.logger.info(message)
        
        if str(actual_value) != str(expected_value):
            error_msg = f"Assertion failed - {assertion_description}"
            logger.error(error_msg)
            self.logger.error(error_msg)
