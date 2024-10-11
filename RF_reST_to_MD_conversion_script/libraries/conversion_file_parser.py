import os

_file_contents=""

def return_or_get_file_contents(file_full_name:str) -> str:   
    global _file_contents
    if not _file_contents:
        try:
            with open(file_full_name) as f: _file_contents = f.read()
        except FileNotFoundError:
            raise # bubble exception
    return _file_contents

# return_or_get_file_contents uses a singleton type approach to read a file once then 
# reuse it's contents - for headings replacement, notes replacement, table replacement etc. 
# However, when the file is finished converting & written out, this needs calling prior to
# switching to any new/alternative/next file to process.
def clear_file_contents_variable():
    global _file_contents
    _file_contents=""

# Should be privately set with "_" underscore but has an associated unit test
def get_file_contents_split_by_lines(file_full_name:str) -> list[str]:   
    _file_contents = return_or_get_file_contents(file_full_name)
    return _file_contents.splitlines(keepends=False)

# Case sensitive search with left & right trim of the text line
def _line_matches_sought_start(line_text:str, block_start:str) -> bool:
    return line_text.strip().__eq__(block_start)

# Case sensitive search with left & right trim of the text line
def _line_matches_sought_end(line_text:str, block_end:str) -> bool:
    return line_text.strip().__eq__(block_end)

def locate_file_content_text_block_instances(file_lines:list[str], block_start:str, block_end:str="") -> list:
    located_blocks = [] 
    located_block_count = 0
    search_block_end = False
    
    #TODO: perhaps ast or list comprehensions are the more pythonic preferred way for this
    for i, line in enumerate(file_lines, 1):
        if _line_matches_sought_start(line, block_start):
            located_blocks.insert(located_block_count,[i])
            print(located_blocks)
            search_block_end = True
        elif search_block_end and i != int(located_blocks[located_block_count][0])+1 and _line_matches_sought_end(line, block_end):
            located_blocks[located_block_count].append(i)
            search_block_end = False
            located_block_count+=1
    print(located_blocks)
    print("**************************************")
    return located_blocks