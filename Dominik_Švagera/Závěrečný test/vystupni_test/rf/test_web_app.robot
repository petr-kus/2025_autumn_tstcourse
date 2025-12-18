*** Settings ***
Library           SeleniumLibrary
Library           ./resources/WebAppLibrary.py
Resource          ./resources/keywords.robot

Suite Setup       Setup Test Suite
Suite Teardown    Teardown Test Suite
Test Setup        Open Browser To Login Page
Test Teardown     Close Browser

*** Variables ***
${URL}              https://www.saucedemo.com/
${BROWSER}          Chrome
${STANDARD_USER}    standard_user
${PROBLEM_USER}     problem_user
${PASSWORD}         secret_sauce

*** Test Cases ***
Test Successful Login And Cart Operations
    [Tags]    smoke    regression
    
    Log    Starting test: Successful Login And Cart Operations    INFO
    
    Page Should Contain Element    id:user-name
    Log    Login page loaded successfully    INFO
    
    Login With Credentials    ${STANDARD_USER}    ${PASSWORD}
    
    Verify Inventory Page Loaded
    ${product_count}=    Get Product Count
    Log    Found ${product_count} products on inventory page    INFO
    Should Be True    ${product_count} > 0    No products found on inventory page
    
    ${product_names}=    Get All Product Names
    Log    Available products: ${product_names}    INFO
    
    Add All Products To Cart
    Log    All products added to cart    INFO
    
    ${cart_badge}=    Get Cart Badge Count
    Log    Cart badge shows: ${cart_badge} items    INFO
    Should Be Equal As Integers    ${cart_badge}    ${product_count}
    
    Open Shopping Cart
    
    Verify Cart Page Loaded
    ${cart_items}=    Get Cart Item Count
    Should Be Equal As Integers    ${cart_items}    ${product_count}
    
    ${products_in_cart}=    Get Product Names In Cart
    Log    Products in cart: ${products_in_cart}    INFO
    
    FOR    ${product}    IN    @{product_names}
        Verify Product In Cart    ${product}
    END
    
    Log    Test completed successfully    INFO

Test Filter Products And Add To Cart
    [Tags]    regression
    
    Log    Starting test: Filter Products And Add To Cart    INFO
    
    Login With Credentials    ${STANDARD_USER}    ${PASSWORD}
    Verify Inventory Page Loaded
    
    Log    Testing product filter: Price (high to low)    INFO
    Apply Product Filter    hilo
    Verify Filter Applied    Price (high to low)
    
    ${products_after_filter}=    Get All Product Names
    Log    Products after filtering: ${products_after_filter}    INFO
    
    ${num_to_add}=    Set Variable    3
    ${product_count}=    Get Product Count
    ${num_to_add}=    Evaluate    min(${num_to_add}, ${product_count})
    
    Log    Adding ${num_to_add} products to cart    INFO
    Add Multiple Products To Cart    ${num_to_add}
    
    ${cart_badge}=    Get Cart Badge Count
    Should Be Equal As Integers    ${cart_badge}    ${num_to_add}
    
    Open Shopping Cart
    Verify Cart Page Loaded
    ${cart_items}=    Get Cart Item Count
    Should Be Equal As Integers    ${cart_items}    ${num_to_add}
    
    Log    Test completed successfully    INFO

Test Problem User Login And Cart
    [Tags]    regression    problem_user
    
    Log    Starting test: Problem User Login And Cart    WARN
    Log    Testing with problem_user - bugs may be encountered    WARN
    
    Login With Credentials    ${PROBLEM_USER}    ${PASSWORD}
    Verify Inventory Page Loaded
    
    Add All Products To Cart
    
    Open Shopping Cart
    Verify Cart Page Loaded
    
    ${cart_items}=    Get Cart Item Count
    Should Be True    ${cart_items} > 0    Cart is empty
    
    ${products_in_cart}=    Get Product Names In Cart
    Log    Problem user cart contains: ${products_in_cart}    INFO
    
    Log    Test completed - problem_user behaved correctly    INFO
