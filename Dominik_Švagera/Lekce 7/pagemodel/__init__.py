"""
Page Object Model pro SauceDemo
Tento balíček obsahuje všechny Page Objects pro automatizované testování.
"""

from .login import LoginPage
from .inventory import InventoryPage
from .cart import CartPage
from .browser import Browser

__all__ = ['LoginPage', 'InventoryPage', 'CartPage', 'Browser']
