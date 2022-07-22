*** Settings ***
Documentation  User add product to the cart
Resource  ./resource.robot
Library  SeleniumLibrary
Library  OperatingSystem
Test Setup  Run Keywords  Setup driver  Close cookies
Test Teardown  Destroy driver

*** Test Case ***
User add product to the cart
    [Documentation]   Put Testrail Link Here
    [Tags]  testrailid=111
    Click category  2
    Click sub category  2
    Hover over item  2
    Click add to cart  2
    Change item entity to  5
    ${item name}=  grab item name
    ${item price}=  grab item price
    Click add item to card
    Click go to cart
    ${cart name}=  get product name
    ${cart price}=  get product price
    Should be equal  ${item name}  ${cart name}
    Should be equal  ${item price}  ${cart price}



