# Lekce 7 - Page Object Model (POM)
# Vysvětlení struktury...
# Struktura projektu

Lekce 7/
├── pagemodel/              # Složka s Page Object Model třídami
│   ├── __init__.py        # Inicializace balíčku (umožňuje importy)
│   ├── login.py           # Page Object pro přihlašovací stránku
│   ├── inventory.py       # Page Object pro stránku s produkty
│   ├── cart.py            # Page Object pro stránku košíku
│   └── browser.py         # Page Object pro správu prohlížeče
├── test.py                # Hlavní testovací soubor s test scénáři
└── README.md              # Tento soubor - vysvětlivka