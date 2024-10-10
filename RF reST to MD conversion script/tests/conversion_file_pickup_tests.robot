get_all_files_for_conversion
*** Settings ***
Library     ../libraries/conversion_file_pickup.py
Variables   conversion_file_pickup_test_data.py


*** Test Cases ***
get all files for conversion test
    ${result}=    Get All File Names    files_for_testing
    Should Be Equal    ${result}    ${all_file_names_expected}
    
get single file name for conversion test
    ${result}=    Get Single File Name    files_for_testing    small_data_file.txt
    Should Contain    ${result}    resources\\files_for_testing\\small_data_file.txt