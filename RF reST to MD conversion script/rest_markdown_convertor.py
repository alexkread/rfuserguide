import re


# def convert_heading(line_of_text:str):
#     after_digits_pattern=r'([\s]{3}|\t])([a-zA-Z]{1}.+)$'
#     three_digits_pattern=r'^(\d{1}.\d{1}.\d{1})' + after_digits_pattern
#     if (re.match(three_digits_pattern, line_of_text) != None):
#         return re.sub(three_digits_pattern, r'### \3', line_of_text)
#     else:
#         two_digits_pattern=r'^(\d{1}.\d{1})' + after_digits_pattern
#         if (re.match(two_digits_pattern, line_of_text) != None):
#             return re.sub(two_digits_pattern, r'## \3', line_of_text)
#         else:
#             one_digit_pattern=r'^(\d{1})' + after_digits_pattern
#             if (re.match(one_digit_pattern, line_of_text) != None):
#                 return re.sub(one_digit_pattern, r'# \3', line_of_text)
#             else:
#                 return line_of_text



def convert_heading(line_of_text:str):
    after_digits_pattern=r'([\s]{3}|\t])([a-zA-Z]{1}.+)$'
    list = [[r'^(\d{1}.\d{1}.\d{1})' + after_digits_pattern, r'### \3'], 
            [r'^(\d{1}.\d{1})' + after_digits_pattern, r'## \3'],
            [r'^(\d{1})' + after_digits_pattern, r'# \3']]
    
    for row in list:
        if (re.match(row[0], line_of_text) != None):
            return re.sub(row[0], row[1], line_of_text)
        
    return line_of_text


