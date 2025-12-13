*** Settings ***
Library           SeleniumLibrary
Library           Collections

*** Keywords ***
Setup Test Suite
    Log    Test suite starting    INFO
    Set Selenium Speed    0.3 seconds
    Set Selenium Timeout    10 seconds

Teardown Test Suite
    Log    Test suite completed    INFO

Open Browser To Login Page
    [Arguments]    ${url}=https://www.saucedemo.com/    ${browser}=Chrome
    Log    Opening browser: ${browser}    INFO
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Log    Browser opened successfully    INFO

Login With Credentials
    [Arguments]    ${username}    ${password}
    Log    Attempting login with username: ${username}    INFO
    Input Text    id:user-name    ${username}
    Input Password    id:password    ${password}
    Click Button    id:login-button
    Log    Login credentials submitted    INFO

Verify Inventory Page Loaded
    Location Should Contain    inventory
    Wait Until Page Contains Element    id:inventory_container
    Log    Inventory page loaded successfully    INFO

Verify Cart Page Loaded
    Location Should Contain    cart
    Wait Until Page Contains Element    id:cart_contents_container
    Log    Cart page loaded successfully    INFO

Get Product Count
    ${count}=    Get Element Count    class:inventory_item
    Log    Found ${count} products    DEBUG
    RETURN    ${count}

Get All Product Names
    @{elements}=    Get WebElements    class:inventory_item_name
    @{names}=    Create List
    FOR    ${element}    IN    @{elements}
        ${text}=    Get Text    ${element}
        Append To List    ${names}    ${text}
    END
    Log    Product names: ${names}    DEBUG
    RETURN    ${names}

Add All Products To Cart
    @{buttons}=    Get WebElements    css:button[id^='add-to-cart']
    ${count}=    Get Length    ${buttons}
    Log    Adding ${count} products to cart    INFO
    FOR    ${button}    IN    @{buttons}
        Click Element    ${button}
    END
    Log    All products added to cart    DEBUG

Add Multiple Products To Cart
    [Arguments]    ${count}
    @{buttons}=    Get WebElements    css:button[id^='add-to-cart']
    FOR    ${index}    IN RANGE    ${count}
        ${button}=    Get From List    ${buttons}    ${index}
        Click Element    ${button}
        Log    Added product ${index + 1} to cart    DEBUG
    END

Apply Product Filter
    [Arguments]    ${filter_value}
    Log    Applying filter: ${filter_value}    INFO
    Select From List By Value    class:product_sort_container    ${filter_value}
    Log    Filter applied    DEBUG

Verify Filter Applied
    [Arguments]    ${expected_text}
    ${selected}=    Get Selected List Label    class:product_sort_container
    Should Be Equal    ${selected}    ${expected_text}
    Log    Filter verified: ${expected_text}    INFO

Get Cart Badge Count
    ${count}=    Run Keyword And Return Status    Page Should Contain Element    class:shopping_cart_badge
    IF    ${count}
        ${text}=    Get Text    class:shopping_cart_badge
        ${number}=    Convert To Integer    ${text}
        Log    Cart badge count: ${number}    DEBUG
        RETURN    ${number}
    ELSE
        Log    Cart badge not present    DEBUG
        RETURN    0
    END

Open Shopping Cart
    Log    Opening shopping cart    INFO
    Click Element    class:shopping_cart_link

Get Cart Item Count
    ${count}=    Get Element Count    class:cart_item
    Log    Cart contains ${count} items    DEBUG
    RETURN    ${count}

Get Product Names In Cart
    @{elements}=    Get WebElements    class:inventory_item_name
    @{names}=    Create List
    FOR    ${element}    IN    @{elements}
        ${text}=    Get Text    ${element}
        Append To List    ${names}    ${text}
    END
    Log    Products in cart: ${names}    INFO
    RETURN    ${names}

Verify Product In Cart
    [Arguments]    ${product_name}
    ${names}=    Get Product Names In Cart
    List Should Contain Value    ${names}    ${product_name}
    Log    Product verified in cart: ${product_name}    DEBUG
