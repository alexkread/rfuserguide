import re


def convert_heading(line_of_text:str):
    after_digits_pattern=r'([\s]{3}|\t])([a-zA-Z]{1}.+)$'
    list = [[r'^(\d{1}.\d{1}.\d{1})' + after_digits_pattern, r'### \3'], 
            [r'^(\d{1}.\d{1})' + after_digits_pattern, r'## \3'],
            [r'^(\d{1})' + after_digits_pattern, r'# \3']]
    
    for row in list:
        if (re.match(row[0], line_of_text) != None):
            return re.sub(row[0], row[1], line_of_text)
        
    return line_of_text


