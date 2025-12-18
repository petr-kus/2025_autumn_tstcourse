*** Settings ***
Documentation     RF test - saucedemo.com
Library           ../resources/InventoryPage.py    WITH NAME    Inventory
Library           ../resources/LoginPage.py    WITH NAME    Login
Library           ../resources/Browser.py    WITH NAME    Browser
Library           Screenshot


*** Variables ***
${Page}           https://www.saucedemo.com
${USERNAME}       standard_user
${PASSWORD}       secret_sauce
${BROWSER}        chrome

*** Test Cases ***
Login User
    [Documentation]    Testuje přihlášení uživatele na stránce
    Browser.Open Browser
    Browser.Get Driver
    Login.Open Login Page     
    Login.Login User    ${USERNAME}    ${PASSWORD}
    Browser.Take Screenshot     after_login.png

Add Random Product To Cart
    ${products}    Inventory.Display Products
    ${product}     Inventory.Select Random Product     ${products}
    ${name}        Inventory.Add Product To Cart     ${product}
    Browser.Take Screenshot    after_add_product_to_cart
    ${count}       Inventory.Get Cart Items Count
    Should Be Equal As Integers    ${count}     1
    Go To Cart
    Inventory.Go Back
    
    
Product Detail Displays Correct Image And Name  
    ${products}    Inventory.Display Products
    ${product}    Inventory.Select Random Product    ${products}

    ${product_name}     Get Product Name Text  ${product}

    ${src}    Inventory.Click Product Image    ${product}
    ${detail_img}    Inventory.Get Product Detail Image Src
    Should Be Equal    ${src}    ${detail_img}
    Inventory.Go Back

    ${products}    Inventory.Display Products
    ${product}    Inventory.Select Random Product    ${products}
    ${name}    Inventory.Click Product Name    ${product}
    ${detail_name}    Inventory.Get Product Detail Name
    Should Be Equal    ${name}    ${detail_name}


