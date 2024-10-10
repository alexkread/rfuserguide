*** Settings ***
Library     ../libraries/convert_token.py
Variables   token_test_data.py


# *** Test Cases ***
# convert reST note test
#    [Documentation]    Applies to original online userguide reST format text
#    Log  \n${three_digit_heading_text}  console=yes
#    Log  ${single_text_rest_note_line_break_after}  console=yes
    #${result}=    convert_rest_note    ${three_digit_heading_text}
    #${result}=    convert_rest_note    ${single_text_rest_note_line_break_after}
    #Should Be Equal    ${result}    ${single_text_rest_note_line_break_after_expected}
    
# convert markdown note test
#    [Documentation]    Applies to already-converted but pre-MKDocs text in chapters 1+2
#    Return From Keyword
    #${result}=    convert_pre_mkdocs_note    ${three_digit_heading_text}
    #Should Be Equal    ${result}    ${three_digit_heading_expected}
