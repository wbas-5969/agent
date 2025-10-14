import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    # If any errors are raised by the standard library functions, catch them and instead return a string describing the error. Always prefix error strings with "Error:".
    # print(f"working_directory: {working_directory}")
    # print(f"directory: {directory}")
    
    my_directory = os.path.abspath(os.path.join(os.path.abspath(working_directory), directory))
    # print(f"my_directory: {my_directory}")
    # If the absolute path to the directory is outside the working_directory, return a string error message:
    dir_abspath = os.path.abspath(working_directory)
    # print(f"dir_abspath: {dir_abspath}")
    if not my_directory.startswith(dir_abspath):
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    # If the directory argument is not a directory, again, return an error string:
    if not os.path.isdir(my_directory):
        return(f'Error: "{my_directory}" is not a directory')

    # Build and return a string representing the contents of the directory. It should use this format:
        # - README.md: file_size=1032 bytes, is_dir=False
        # - src: file_size=128 bytes, is_dir=True
        # - package.json: file_size=1234 bytes, is_dir=False
    dir_listing = os.listdir(my_directory)
    return_string = ""
    full_path = ""
    file_name = ""
    file_size = ""
    is_dir = ""
    for dir_item in dir_listing:
        full_path = os.path.join(my_directory, dir_item)
        file_name = dir_item
        if os.path.isdir(full_path):
            is_dir = "is_dir=True"
        else:
            is_dir = "is_dir=False"
        
        file_size = os.path.getsize(full_path)
        file_size = f"file_size={file_size}"

        file_name = dir_item
        return_string = return_string + f"{file_name}: {file_size} bytes, {is_dir}\n"

    return return_string.rstrip("\n")
    