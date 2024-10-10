get_all_files_for_conversion
*** Settings ***
Library     ../libraries/conversion_file_parser.py
Library     ../libraries/conversion_file_pickup.py
Variables   conversion_file_parser_test_data.py


*** Test Cases ***
get file contents test
    ${file_name}=    Get Single File Name    files_for_testing    small_data_file.txt
    ${result}=    Return Or Get File Contents   ${file_name}
    Should Be Equal As Strings    ${result}    ${file_contents_expected}

get file contents split by lines test
    ${file_name}=    Get Single File Name    files_for_testing    small_data_file.txt
    ${result}=    Get File Contents Split By Lines   ${file_name}
    Should Be Equal As Strings    ${result}    ${file_contents_split_by_lines_expected}

locate file content text block instances test
    Clear File Contents Variable
    ${file_name}=    Get Single File Name    files_for_testing    medium_data_file_with_text_blocks.txt
    ${result}=    Locate File Content Text Block Instances   ${file_name}    Note:
    Should Be Equal    ${result}    ${file_content_note_blocks_expected}
