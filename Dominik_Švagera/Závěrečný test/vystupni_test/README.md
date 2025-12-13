# Web Application Test Automation

## Project Structure

```
vystupni_test/
├── install_dependencies.ps1    # Dependency installation script
├── pytest/                      # PyTest implementation
│   ├── pagemodel/              # Page Object Model classes
│   │   ├── __init__.py
│   │   ├── login_page.py       # Login page POM
│   │   ├── inventory_page.py   # Inventory page POM
│   │   └── cart_page.py        # Cart page POM
│   ├── logs/                   # Test execution logs (auto-created)
│   ├── conftest.py             # PyTest fixtures and configuration
│   ├── pytest.ini              # PyTest configuration
│   ├── test_web_app.py         # Test cases
│   └── requirements.txt        # Python dependencies
└── rf/                         # Robot Framework implementation
    ├── resources/              # RF keywords and libraries
    │   ├── keywords.robot      # Reusable keywords
    │   └── WebAppLibrary.py    # Custom Python library
    ├── logs/                   # Test execution logs (auto-created)
    ├── test_web_app.robot      # Test cases
    └── requirements.txt        # Python dependencies
```

## Installation

Run the installation script from PowerShell:

```powershell
cd vystupni_test
.\install_dependencies.ps1
```

The script will:
- Verify Python and pip installation
- Install all PyTest dependencies
- Install all Robot Framework dependencies
- Verify installations

## Running Tests

### PyTest

Using PowerShell script:
```powershell
cd vystupni_test\pytest
.\run_tests.ps1
```

Or manually:
```powershell
cd vystupni_test\pytest
python -m pytest -v
```

Run specific test:
```powershell
python -m pytest test_web_app.py::TestLoginAndCart::test_successful_login_and_cart_operations
```

### Robot Framework

Using PowerShell script:
```powershell
cd vystupni_test\rf
.\run_tests.ps1
```

Or manually:
```powershell
cd vystupni_test\rf
python -m robot -d logs test_web_app.robot
```

Run specific test:
```powershell
python -m robot -t "Test Successful Login And Cart Operations" -d logs test_web_app.robot
```

## Test Coverage

Both implementations test the same scenarios:

1. **Successful Login And Cart Operations**
   - User login with standard credentials
   - Verify inventory page loads
   - Add all products to cart
   - Verify cart contents

2. **Filter Products And Add To Cart**
   - User login
   - Apply product filter (price high to low)
   - Add filtered products to cart
   - Verify cart

3. **Problem User Login And Cart**
   - Login with alternative user account
   - Add products to cart
   - Verify cart

## Key Features

### PyTest Implementation
- Page Object Model pattern with separate classes
- Comprehensive logging to file with timestamps
- DEBUG level for input data and internal operations
- INFO level for user actions and verification
- ERROR level for exceptions with full stack traces
- Pytest hooks for automatic test result logging
- WebDriver auto-management with webdriver-manager

### Robot Framework Implementation
- Custom keywords for reusability
- Python library for enhanced logging
- Built-in HTML reports
- Keyword-driven test structure
- Separate resources for maintainability

## Logging

### PyTest
Logs are written to `pytest/logs/test_run_YYYYMMDD_HHMMSS.log`
- Contains DEBUG, INFO, and ERROR level messages
- Includes test execution flow and results
- Exception stack traces for failures

### Robot Framework
Logs are written to:
- `rf/logs/robot_test_YYYYMMDD_HHMMSS.log` (Python library logs)
- `log.html` (Robot Framework HTML log)
- `report.html` (Robot Framework HTML report)
- `output.xml` (Robot Framework XML output)

