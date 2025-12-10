*** Settings ***
Documentation     Saucedemo – Robot Framework test (login, košík, logout)
Library           pagemodel/Browser.py
Library           pagemodel/LoginPage.py
Library           pagemodel/InventoryPage.py
Library           Screenshot

*** Variables ***
${PAGE}           https://www.saucedemo.com/
${STANDARD_USER}  standard_user
${PROBLEM_USER}   problem_user
${PASSWORD}       secret_sauce

*** Test Cases ***
Cart badge behavior
    [Documentation]    Po přidání batohu do košíku se u ikonky košíku zobrazí číslo 1
    ${browser}    Browser is running
    Open ${PAGE} in ${browser}
    Login User    ${STANDARD_USER}    ${PASSWORD}
    Add backpack to cart in ${browser}
    Cart badge should show 1 in ${browser}

Login User
    [Documentation]    Ukázka [Template] – login + logout pro různé uživatele
    [Template]    Login User Template
    ${PAGE}    ${STANDARD_USER}    ${PASSWORD}
    ${PAGE}    ${PROBLEM_USER}    ${PASSWORD}

Logout user
    [Documentation]    Odhlášení uživatele přes menu
    ${browser}    Browser is running
    Open ${PAGE} in ${browser}
    Login User    ${STANDARD_USER}    ${PASSWORD}
    Logout via menu in ${browser}

*** Keywords ***
Login User Template
    [Arguments]    ${page}    ${username}    ${password}
    ${browser}    Browser is running
    Open ${page} in ${browser}
    Login User    ${username}    ${password}
