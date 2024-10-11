*** Settings ***
Library     ../libraries/convert_token.py
Library     ../libraries/conversion_file_parser.py
Library     ../libraries/conversion_file_pickup.py
Variables   token_test_data.py


*** Test Cases ***
convert reST note test
   [Documentation]    Applies to original online userguide reST format text
   Log  \n${three_digit_heading_text}  console=yes
   Log  ${single_text_rest_note_line_break_after}  console=yes
   
    Clear File Contents Variable
    ${file_name}=    Get Single File Name    files_for_testing    medium_data_file_with_text_blocks.txt
    ${result}=    Locate File Content Text Block Instances   ${file_name}    Note:
    #Should Be Equal    ${result}    ${file_content_note_blocks_expected}
    
# convert markdown note test
#    [Documentation]    Applies to already-converted but pre-MKDocs text in chapters 1+2
#    Return From Keyword
    #${result}=    convert_pre_mkdocs_note    ${three_digit_heading_text}
    #Should Be Equal    ${result}    ${three_digit_heading_expected}
