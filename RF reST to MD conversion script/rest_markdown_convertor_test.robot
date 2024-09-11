*** Settings ***
Library     rest_markdown_convertor.py
Variables   rest_markdown_convertor_test_data.py


*** Test Cases ***
Convert heading three digits test
    ${result}=    convert heading    ${three_digit_heading_text}
    Should Be Equal    ${result}    ${three_digit_heading_expected}
    

Convert heading two digits test
    ${result}=    convert heading    ${two_digit_heading_text}
    Should Be Equal    ${result}    ${two_digit_heading_expected}
    

Convert heading one digit test
    ${result}=    convert heading    ${one_digit_heading_text}
    Should Be Equal    ${result}    ${one_digit_heading_expected}
    

Convert heading no digits test
    ${result}=    convert heading    ${no_digit_heading_text}
    Should Be Equal    ${result}    ${no_digit_heading_text}


Convert heading empty input string test
    ${result}=    convert heading    ${EMPTY}
    Should Be Equal    ${result}    ${EMPTY}
