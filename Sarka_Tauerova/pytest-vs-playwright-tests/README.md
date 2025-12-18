# PyTest vs Playwright – End-to-End Test Comparison

Tento repozitář obsahuje **srovnání jednoho testovacího scénáře**
implementovaného ve **dvou různých testovacích frameworcích**:

- **PyTest (Python)**
- **Playwright (Microsoft framework)**

Cílem projektu je ukázat:
- rozdíly v přístupu k automatizovanému testování,
- strukturování testů,
- čitelnost Domain Language,
- práci s Page Object Model (POM),
- a chování testu na bezchybném vs. zabugovaném účtu.

Projekt vznikl jako **výstupní testovací úkol** a zároveň slouží
jako **referenční ukázka pro budoucí praxi**.

---

## Struktura projektu

```text
pytest-vs-playwright-tests/
├─ pytest/
│  ├─ pages/
│  ├─ tests/
│  ├─ conftest.py
│  ├─ pytest.ini
│  ├─ requirements.txt
│  ├─ install_dependencies.ps1
│  └─ README.md
│
├─ playwright/
│  ├─ pages/
│  ├─ tests/
│  ├─ install_dependencies.ps1
│  └─ README.md
│
└─ README.md
```
---

## Testovací scénář (společný pro oba frameworky)

- jeden a ten samý test case,
- práce minimálně se **dvěma stránkami aplikace**,
- test:
  - **prochází na bezchybném účtu**,
  - **selhává na zabugovaném účtu** (očekávané selhání),
- důraz na:
  - čitelnost testu,
  - srozumitelné pojmenování kroků,
  - jasné vyjádření záměru testu.

---

## Použité přístupy a principy

- Page Object Model (POM)
- Domain Language (čitelné názvy metod a kroků)
- Oddělení:
  - testovací logiky,
  - testovacích dat,
  - infrastruktury testů
- Ověřování **očekávaného selhání testu**
- Čistá struktura projektu bez zbytečné složitosti

---

## Jak s projektem pracovat

Každá implementace má **vlastní dokumentaci**:

- 📂 **PyTest verze**  
  → otevři `pytest/README.md`

- 📂 **Playwright verze**  
  → otevři `playwright/README.md`

V jednotlivých README je vždy popsáno:
- jak projekt spustit,
- jaké jsou závislosti,
- jak test funguje a co ověřuje.

---

## Poznámka

Tento repozitář není zaměřen na konkrétní testovanou aplikaci,
ale na **kvalitu návrhu testů, strukturu a čitelnost řešení**.

Slouží jako:
- studijní materiál,
- srovnávací ukázka frameworků,
- a podklad pro další profesní použití.