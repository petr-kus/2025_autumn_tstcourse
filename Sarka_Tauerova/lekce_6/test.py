from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# ==========================
# DEBUG SWITCH (True/False)
# ==========================
DEBUG_SLOW = True
SLOW_DELAY = 1.0  # seconds

def slow_pause():
    if DEBUG_SLOW:
        time.sleep(SLOW_DELAY)

def slow_click(driver, element):
    slow_pause()
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior:'smooth',block:'center'});", element
    )
    slow_pause()
    driver.execute_script("arguments[0].click();", element)
    slow_pause()

def slow_type(element, text):
    if DEBUG_SLOW:
        for char in text:
            element.send_keys(char)
            time.sleep(0.08)
    else:
        element.send_keys(text)

# ==========================
# BROWSER SETUP
# ==========================
options = Options()
options.add_argument("start-maximized")
options.add_argument("--guest")

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

# ==========================
# LOGIN
# ==========================
username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
slow_type(username, "standard_user")

password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
slow_type(password, "secret_sauce")

login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
slow_click(driver, login_btn)

wait.until(EC.url_contains("inventory"))

# ==========================
# SELECT 4 RANDOM PRODUCTS
# ==========================
buttons = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(),'Add to cart')]"))
)

selected_products = random.sample(buttons, 4)

for i, btn in enumerate(selected_products, start=1):
    print(f"Adding product number {i}")
    slow_click(driver, btn)

# ==========================
# CART & CHECKOUT
# ==========================
cart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
slow_click(driver, cart)

checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
slow_click(driver, checkout_btn)

# ==========================
# CHECKOUT FORM
# ==========================
first = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
slow_type(first, "Sarka")

last = wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
slow_type(last, "Tester")

zip_code = wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
slow_type(zip_code, "12345")

continue_btn = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
slow_click(driver, continue_btn)

finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
slow_click(driver, finish_btn)

# ==========================
# VALIDATION
# ==========================
success = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text

if "THANK YOU" in success.upper():
    print("TEST PASSED — order completed successfully.")
else:
    print("TEST FAILED — confirmation message not found.")

# ==========================
# LOGOUT
# ==========================
menu_btn = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
slow_click(driver, menu_btn)

logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")))
slow_click(driver, logout_btn)

print("Logout completed.")
driver.quit()
