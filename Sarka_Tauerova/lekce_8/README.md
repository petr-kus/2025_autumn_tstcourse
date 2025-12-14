# Lekce 8 – Automatizované testy (Pytest + Page Object Model)

Tento projekt obsahuje řešení úkolu z **lekce 8** kurzu automatizovaného testování.  
Cílem je strukturovat testy pomocí **Page Object Modelu (POM)** a **pytestu** tak,
aby byly čitelné, rozšiřitelné a snadno udržovatelné.

---
## Použité principy
- Page Object Model (POM)
- Pytest + fixtures
- Parametrizace testů
- Oddělení testovací logiky a testovacích dat
- Čitelný „Domain Language“ v testech

---
## Struktura projektu
```text
lekce_8/
├─ pages/
│  ├─ base_page.py
│  ├─ burger_menu.py
│  ├─ cart_page.py
│  ├─ checkout_page.py
│  ├─ header.py
│  ├─ inventory_page.py
│  └─ login_page.py
├─ tests/
│  ├─ test_login.py
│  ├─ test_problem_user.py
│  └─ test_purchase_flow.py
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
├─ install_dependencies.ps1
└─ README.md
```
---
## Instalace a prostředí
V adresáři projektu je připraven PowerShell skript:
install_dependencies.ps1

Skript provede:
- vytvoření virtuálního prostředí,
- instalaci potřebných balíčků,
- uložení závislostí do `requirements.txt`.

---
## Spuštění testů
1. Aktivuj virtuální prostředí:
.\venv\Scripts\Activate.ps1

2. Spusť testy:
pytest

Nastavení pytestu:
- zapnuté logování na úrovni `INFO`,
- testy se zastaví při první chybě,
- výstup je zkrácený a přehledný.

---

## Chování testů
- **locked_out_user**  
  Negativní scénář – očekává se chyba při přihlášení.

- **problem_user**  
  Negativní scénář – checkout nesmí být úspěšně dokončen.

- **performance_glitch_user**  
  Známá chyba aplikace:
  - badge v košíku může zobrazovat nesprávný počet položek,
  - test proto ověřuje skutečný obsah košíku,
  - test je označen jako `xfail` (očekávané selhání).

---
## Poznámka
Projekt je strukturován tak, aby bylo možné snadno:
- přidat další testovací scénáře,
- rozšířit Page Objecty,
- pracovat s různými typy uživatelů bez duplikace kódu.