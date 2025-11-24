import logging
from datetime import datetime
import os
from pagemodel import LoginPage, InventoryPage, CartPage, Browser


script_dir = os.path.dirname(os.path.abspath(__file__))
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = os.path.join(script_dir, f"test_log_{timestamp}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)



def test_standard_user_can_login_filter_products_and_add_all_to_cart():
    """
    Test: Standardní uživatel se přihlásí do SauceDemo e-shopu, otestuje všechny filtry produktů,
    přidá všechny dostupné produkty do košíku a ověří, že jsou v košíku správně zobrazeny
    """
    logger.info("=== TEST: Standardní uživatel - kompletní nákupní flow ===")
    
    driver = Browser.start()
    
    try:
        # Given - Otevřu SauceDemo e-shop
        login_page = LoginPage(driver)
        login_page.open().verify_page_is_loaded()
        
        # When - Přihlásím se jako standardní uživatel
        inventory_page = login_page.login_as("standard_user", "secret_sauce")
        
        # Then - Jsem přihlášen a vidím katalog produktů
        inventory_page.verify_user_is_logged_in()
        
        # When - Otestuji všechny filtry řazení produktů (A-Z, Z-A, cena)
        inventory_page.test_all_product_sorting_filters()
        
        # When - Přidám všechny dostupné produkty do nákupního košíku
        inventory_page.add_all_products_to_cart()
        
        # When - Otevřu nákupní košík
        cart_page = inventory_page.open_cart()
        
        # Then - Košík je otevřený a obsahuje všechny přidané produkty
        cart_page.verify_cart_page_is_open().verify_cart_contains_products()
        
        logger.info("TEST ÚSPĚŠNÝ")
        
    except AssertionError as e:
        logger.error("TEST SELHAL")
        logger.error(f"Důvod selhání: {e}")
        raise
    except Exception as e:
        logger.error("TEST SELHAL - Neočekávaná chyba")
        logger.error(f"Chyba: {e}", exc_info=True)
        raise
    finally:
        Browser.stop(driver)


def test_problem_user_can_complete_shopping_despite_known_issues():
    """
    Test: Problémový uživatel (problem_user) se přihlásí do SauceDemo e-shopu a provede
    kompletní nákupní proces včetně filtrování a přidání produktů - ověřuje, že základní
    funkce fungují i přes známé problémy s tímto účtem
    """
    logger.info("=== TEST: Problémový uživatel - testování odolnosti systému ===")
    
    driver = Browser.start()
    
    try:
        # Given - Otevřu SauceDemo e-shop
        login_page = LoginPage(driver)
        login_page.open().verify_page_is_loaded()
        
        # When - Přihlásím se jako problémový uživatel (known issues)
        inventory_page = login_page.login_as("problem_user", "secret_sauce")
        
        # Then - Jsem přihlášen i přes možné problémy s účtem
        inventory_page.verify_user_is_logged_in()
        
        # When - Otestuji všechny filtry řazení (může selhat kvůli problémovému účtu)
        inventory_page.test_all_product_sorting_filters()
        
        # When - Pokusím se přidat všechny produkty do košíku
        inventory_page.add_all_products_to_cart()
        
        # When - Otevřu nákupní košík
        cart_page = inventory_page.open_cart()
        
        # Then - Ověřím, že košík obsahuje produkty (i přes problémový účet)
        cart_page.verify_cart_page_is_open().verify_cart_contains_products()
        
        logger.info("TEST ÚSPĚŠNÝ")
        
    except AssertionError as e:
        logger.error("TEST SELHAL")
        logger.error(f"Důvod selhání: {e}")
        raise
    except Exception as e:
        logger.error("TEST SELHAL - Neočekávaná chyba")
        logger.error(f"Chyba: {e}", exc_info=True)
        raise
    finally:
        Browser.stop(driver)


if __name__ == "__main__":
    logger.info("\n" + "="*80)
    logger.info("ZAHÁJENÍ TESTOVÁNÍ")
    logger.info("="*80 + "\n")
    
    # Spuštění testů
    test_standard_user_can_login_filter_products_and_add_all_to_cart()
    print("\n" + "-"*80 + "\n")
    test_problem_user_can_complete_shopping_despite_known_issues()
    
    logger.info("\n" + "="*80)
    logger.info("TESTOVÁNÍ DOKONČENO")
    logger.info("="*80)