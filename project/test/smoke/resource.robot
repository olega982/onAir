*** Settings ***
Resource  ../../resource/resource.robot

*** Keywords ***
setup driver
    [Timeout]  1min
    CommonSteps.create driver

close cookies
    CommonSteps.close cookies

destroy driver
    CommonSteps.destroy driver