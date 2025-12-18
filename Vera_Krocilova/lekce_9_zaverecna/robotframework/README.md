```markdown

# Automatizované testy – Robot Framework

Tento adresář obsahuje testy napsané v *Robot Framework* pro demo aplikaci
`https://www.saucedemo.com/`. Testy používají vlastní knihovny umístěné ve
`resources/` (např. `Browser.py`, `LoginPage.py`, `InventoryPage.py`) a standardní
Robot knihovnu `Screenshot` pro ukládání snímků obrazovky.

---

## Použité technologie a závislosti

- Python 3.8+
- Robot Framework
- Selenium (použito v `resources/Browser.py`)
- webdriver-manager pro pohodlné použití ovladače 

Závislosti jsou uvedeny v `requirements.txt`. Pro rychlou instalaci na Windows
je k dispozici skript `install_dependencies.ps1`.

---

## Struktura projektu (hlavní složky)

robotframework/
├─ tests/
│ └─ test_saucedemo.robot
├─ resources/
│ ├─ Browser.py
│ ├─ LoginPage.py
│ └─ InventoryPage.py
├─ requirements.txt
├─ install_dependencies.ps1
└─ README.md

---

## O testu `tests/test_saucedemo.robot`

Testy v tomto souboru provádějí tyto kroky (shrnutí):

- otevření prohlížeče a načtení přihlašovací stránky
- přihlášení uživatele 
- zobrazení produktů, výběr náhodného produktu
- přidání produktu do košíku a ověření počtu položek
- kontrola detailu produktu (obrázek a název)

## Spuštění testů

Spustit všechny Robot testy v tomto adresáři:

```powershell
robot .
```

Spustit konkrétní soubor:

```powershell
robot tests/test_saucedemo.robot
```

## Výstupy, logy a screenshoty

- Robot Framework generuje `output.xml`, `log.html` a `report.html` v
	adresáři, odkud testy spouštíte.
- Screenshoty jsou vytvářeny voláním klíčového slova `Browser.Take Screenshot`
	(implementováno v `resources/Browser.py`) a ukládají se do aktuálního
	pracovního adresáře nebo do podsložky dle implementace.

Pro zobrazení reportu po spuštění otevřete `report.html` v prohlížeči.

---

## Nastavení prostředí

1. Vytvořte a aktivujte virtuální prostředí (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Nainstalujte závislosti:

```powershell
pip install -r requirements.txt
```

Nebo použijte `install_dependencies.ps1` pokud je dostupný:

```powershell
.\install_dependencies.ps1
```

---


Uloženo: `Vera_Krocilova/lekce_9_zaverecna/robotframework/README.md`


