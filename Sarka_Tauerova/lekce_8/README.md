# Lekce 8 – Strukturovaný test (POM + pytest)

Tento projekt obsahuje řešení úkolu z **lekce 8**, jehož cílem bylo převést existující testovací scénáře do přehledné a udržovatelné struktury s využitím objektového přístupu.

Projekt je postaven tak, aby bylo snadné:
- přidávat nové testovací scénáře,
- testovat různé typy uživatelů,
- rozšiřovat funkcionalitu bez zásahů do existujících testů.

---

## Použité principy

- **Page Object Model (POM)**
- **Object Oriented Programming (OOP)**
- **pytest + fixtures**
- **Parametrizace testů**
- **Domain Language** (čitelné názvy metod a kroků)

---

## Struktura projektu

lekce_8/
├── pages/ # Page Objecty aplikace
├── tests/ # Testovací scénáře
├── conftest.py # Fixtures a testovací data
├── pytest.ini # Nastavení pytestu
├── requirements.txt
└── README.md

---

## Instalace a prostředí

V adresáři je připraven skript:

install_dependencies.ps1

Skript:
- vytvoří virtuální prostředí,
- nainstaluje potřebné balíčky,
- uloží závislosti do `requirements.txt`.

---

## Spuštění testů

Po aktivaci virtuálního prostředí:

```bash
pytest
Nastavení pytestu:

zapnuté logování (INFO),

testy se zastaví při první chybě,

výstup je zkrácený a přehledný.

Poznámky k chování testů
locked_out_user je negativní scénář – očekává se chyba při loginu.

problem_user je záměrně problematický účet – checkout nesmí projít.

performance_glitch_user má známé UI chyby:

badge v košíku může ukazovat nesprávný počet položek,

test proto ověřuje skutečný obsah košíku, nikoli pouze badge.

Toto chování je vědomé a odpovídá zadání.

Cíl řešení
Cílem nebylo vytvořit „nejkratší test“, ale:

čitelný testovací scénář,

jasně oddělenou logiku,

strukturu připravenou pro další rozšiřování.