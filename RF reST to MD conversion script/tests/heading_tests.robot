*** Settings ***
Library     ../libraries/convert_heading.py
Variables   heading_test_data.py


*** Test Cases ***
convert top level heading three digits test
    ${result}=    Convert Top Level Heading    ${three_digit_heading_text}
    Should Be Equal As Strings    ${result}    ${three_digit_heading_expected}
    

convert top level heading two digits test
    ${result}=    Convert Top Level Heading    ${two_digit_heading_text}
    Should Be Equal As Strings    ${result}    ${two_digit_heading_expected}
    

convert top level heading one digit test
    ${result}=    Convert Top Level Heading    ${one_digit_heading_text}
    Should Be Equal As Strings    ${result}    ${one_digit_heading_expected}
    

convert top level heading no digits test
    ${result}=    Convert Top Level Heading    ${no_digit_heading_text}
    Should Be Equal As Strings    ${result}    ${no_digit_heading_text}


convert top level heading empty input string test
    ${result}=    Convert Top Level Heading    ${EMPTY}
    Should Be Equal As Strings    ${result}    ${EMPTY}
