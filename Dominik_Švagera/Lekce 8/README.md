# Lekce 8 - PyTest Framework + POM

## Struktura projektu

```
Lekce 8/
├── pagemodel/
│   ├── __init__.py
│   ├── login.py        - Přihlašovací stránka
│   ├── inventory.py    - Stránka s produkty
│   └── cart.py         - Nákupní košík
├── conftest.py         - PyTest fixtures (browser)
├── test.py             - Testy
├── pytest.ini          - PyTest konfigurace
└── requirements.txt    - Závislosti
```

## Instalace

```bash
pip install -r requirements.txt
```

## Spuštění testů

```bash
pytest
```

## Spuštění konkrétní třídy testů

```bash
pytest test.py::TestSauceDemoStandardUser
pytest test.py::TestSauceDemoProblemUser
```

## Co je nového v této lekci

### PyTest Framework
- Automatická správa prohlížeče pomocí fixtures
- Lepší reporting a logování
- Snadné spouštění testů
- Jasná struktura testů ve třídách

### Čistý Domain Language
- Žádné komentáře - kód je samo-popisný
- Metody mají jasné názvy popisující akci
- Konstanty pro testovací data v Page Objects
- Oddělení standardního a problémového uživatele

## Testy

### TestSauceDemoStandardUser
`test_standard_user_can_login_filter_products_and_add_all_to_cart`
- Testuje kompletní nákupní flow standardního uživatele
- Přihlášení, filtry, přidání do košíku, ověření

### TestSauceDemoProblemUser  
`test_problem_user_can_complete_shopping_despite_known_issues`
- Testuje odolnost systému s problémovým účtem
- Stejný flow jako standardní uživatel

## Domain Language příklady

```python
login_page.open().verify_swag_labs_is_loaded()
inventory_page = login_page.login_as_standard_user()
inventory_page.verify_user_is_on_products_page()
inventory_page.test_all_product_sorting_filters()
cart_page = inventory_page.open_shopping_cart()
```

Každá metoda jasně říká CO dělá, bez potřeby komentářů.
