```markdown
# Automatizované testy – Pytest

Tento projekt obsahuje automatizované testy webové aplikace vytvořené pomocí
frameworku **Pytest** a knihovny **Selenium**.  
Projekt je součástí úkolu v kurzu automatizovaného testování.

Cílem projektu je ověřit základní funkčnost webové aplikace a ukázat práci
s automatizovanými testy, Page Object Modelem, logováním a screenshoty při chybách.

---

## Použité technologie a knihovny

- Python 3.x
- Pytest
- Selenium WebDriver
- pytest-html
- logging (standardní Python modul)

Konkrétní závislosti jsou uvedeny v souboru `requirements.txt`.

---

### Instalace závislostí pomocí skriptu

Alternativně lze všechny kroky pro přípravu prostředí a instalaci závislostí provést
pomocí skriptu `install_dependencies.ps1`, který je součástí projektu.  

Spuštění v PowerShellu:

```powershell
.\install_dependencies.ps1

## Struktura projektu

Projekt má následující strukturu:

```text
pytest/
├─ tests/
│  ├─ test_saucedemo.py
│  └─ screenshots/
│
├─ pages/
│  ├─ inventory_page.py
│  └─ login_page.py
│
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
└─ README.md


## Specificky k `test_saucedemo.py`

Tato sekce popisuje konkrétní testy a fixture použité v `tests/test_saucedemo.py`.

- Testy cílí demo stránku: `https://www.saucedemo.com/`.
- Výchozí přihlašovací údaje jsou nastaveny v `conftest.py`.

Logy a artefakty:
- Logovací soubor: `test.log` (konfigurace v `conftest.py`).
- Screenshoty: ukládají se voláním `take_screenshot()` v Page objektech; soubory jsou v pracovním adresáři, odkud spouštíte `pytest` (viz `tests/screenshots/`).

### Spuštění testu s HTML reportem

```bash
pytest tests/test_saucedemo.py --html=report_saucedemo.html --self-contained-html


