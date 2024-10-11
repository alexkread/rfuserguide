import re

#def _remove_line_if_blank(lines:list[str], index:int)-> tuple[list[str],bool]:
#    if str(lines[index]).strip() == "":
#        lines.pop(index)
#        return (lines, True)
#    else:
#        return (lines, False)

def _remove_line_if_blank(lines:list[str], index:int)-> list[str]:
    if str(lines[index]).strip() == "":
        lines.pop(index)
    return (lines)     

# Applies to reST userguide text online currently
def convert_rest_note(file_lines:list[str], block_instances:list) -> list[str]:
    for start, end in block_instances:
        replacement_lines= file_lines[start:end]
        print("@@@@@@@@@@@@@@@@@@")
        print(replacement_lines[0])
        replacement_lines[0] = "!!! note"

        j=0
        for i in replacement_lines:
            print(len(replacement_lines)-2)
            print(j)
            print(i)
            print(replacement_lines[j])
            print(replacement_lines[j] == "")
            print(str(replacement_lines[j]).strip() == "")
            j+=1
            print("*******")

        replacement_lines = _remove_line_if_blank(replacement_lines, len(replacement_lines)-1)
        replacement_lines = _remove_line_if_blank(replacement_lines, 1)

        print(replacement_lines)

        file_lines[start:end] = replacement_lines
    return file_lines

# Applies to reST userguide text online currently
def convert_pre_mkdocs_note(text:str):
    return


# check & convert every line (numbered heading)
# locate blocks with start & end 
#   - change 1st line (reST "Note:" to "!!! note")
#   - change 2-3 starting lines & ending lines (pre-MKDocs note, examples, tables)
# replace all instances in whole file (consistent replacement terms)
