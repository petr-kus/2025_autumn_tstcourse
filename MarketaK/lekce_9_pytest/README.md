# Domácí úkol – Saucedemo (Pytest + Selenium + Allure)

Domácí úkol z testování – automatizované UI testy pro stránku [https://www.saucedemo.com](https://www.saucedemo.com)
pomocí **Pytest**, **Selenium WebDriver**, **Page Object Modelu**, logování a **Allure reportů**.

---

## 1. Co projekt umí

- Přihlášení na `https://www.saucedemo.com`:
  - uživatel `standard_user` – očekávaný úspěšný login
  - uživatel `problem_user` – test označený jako `xfail` (očekávaný neúspěch)
- Test přidání produktu (“Sauce Labs Backpack”) do košíku
- Test viditelnosti obrázků produktů na inventory stránce
- Test odhlášení uživatele (logout)
- Použitý **Page Object Model**:
  - `LoginPage` – přihlášení
  - `InventoryPage` – produkty, košík, logout
  - `CartPage` – kontrola položek v košíku
- Logování přes Python logging – výstup se ukládá do `tests.log`
- Generování výstupu pro **Allure report** (složka `allure-results`)



