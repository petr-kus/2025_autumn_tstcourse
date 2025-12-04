*** Settings ***
Documentation     Basic Robot Framework test structure
Library           pagemodel/LoginPage.py
Library           pagemodel/Browser.py
Library	          Screenshot	

*** Variables ***
${page}            https://www.saucedemo.com/
${USERNAME}       standart_user
${PASSWORD}       secret_sauce

*** Test Cases ***
Login User
    [Documentation]    This is an example test case]
    ${browser}  Browser is running
    Then Open ${page} in ${browser}
    Take Screenshot
    And Login User  ${USERNAME}  ${PASSWORD}
    Take Screenshot

Login User
    [Documentation]    This is an example test case]
    [Template]    Login User Template
    https://www.saucedemo.com/  standard_user   secret_sauce
    https://www.saucedemo.com/  standard_user   secret_sauce

*** Keywords ***
Login User Template
    [Arguments]   ${page}    ${username}    ${password}
    ${browser}  Browser is running
    Open ${page} in ${browser}
    Login User  ${username}  ${password}