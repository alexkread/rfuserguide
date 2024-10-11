import os

# Builds then returns all file names in a given subfolder underneath the resources folder 
# OS independent formatted and as full file path + name + extension formats 
def get_all_file_names(resources_subfolder_name:str) -> list[str]:   
    source_directory = os.path.join(os.getcwd(), "resources", resources_subfolder_name)
    return os.listdir(source_directory)

# Builds then returns a single given file name in a given subfolder underneath the resources folder 
# OS independent formatted and as full file path + name + extension format 
def get_single_file_name(resources_subfolder_name:str, file_name:str) -> str:  
    return os.path.join(os.getcwd(), "resources", resources_subfolder_name, file_name) 