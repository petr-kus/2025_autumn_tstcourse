import os
from datetime import datetime
from robot.api.deco import keyword
from pagemodel import Browser


@keyword("Take Screenshot")
def take_screenshot():
    """Uloží screenshot aktuální stránky do složky 'screenshots'."""
    driver = Browser.get_current_browser()
    if driver is None:
        return

    os.makedirs("screenshots", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = os.path.join("screenshots", f"screenshot_{ts}.png")
    driver.save_screenshot(filename)
    return filename
