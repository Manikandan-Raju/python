*** Settings ***
Documentation    Simple Robot Framework example using a Python keyword library.
Library          ../keywords/ExampleLibrary.py

*** Variables ***
${GREETING}    Hello
${NAME}        World

*** Test Cases ***
Greeting Test
    [Documentation]    Build a greeting using a custom Python keyword.
    ${message}=    Create Greeting    ${GREETING}    ${NAME}
    Should Be Equal    ${message}    Hello, World!

Addition Test
    [Documentation]    Verify numeric addition using a Python keyword.
    ${result}=    Add Numbers    7    5
    Should Be Equal As Integers    ${result}    12

List Filtering Test
    [Documentation]    Show how built-in keywords work with lists.
    @{items}=    Create List    1    2    3    4    5
    ${evens}=    Filter Even Numbers    ${items}
    Length Should Be    ${evens}    2
    Should Be Equal As Integers    ${evens[0]}    2
    Should Be Equal As Integers    ${evens[1]}    4
