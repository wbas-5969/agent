import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file_path to the file",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    
    file_relpath= working_directory + "/" + file_path
    file_abspath = os.path.abspath(file_relpath)
    print(f"file_abspath: {file_abspath}")
    dir_abspath = os.path.abspath(working_directory)
    print(f"dir_abspath: {dir_abspath}")
    # If the absolute path to the directory is outside the working_directory, return a string error message:
    if not file_abspath.startswith(dir_abspath):
        return(f'Error: Cannot read "{file_abspath}" as it is outside the permitted working directory')

    # If the directory argument is not a file, again, return an error string:
    try:
        if not os.path.isfile(file_abspath):
            return(f'Error: File not found or is not a regular file: "{file_abspath}"')
    except:
        print(f"Error: system error returned by os.path.isfile({file_abspath})")

    MAX_CHARS = 10000

    with open(file_abspath, "r") as f:
        try:
            file_content_string = f.read(MAX_CHARS)
        except:
            print(f"Error: can't open file: {file_abspath}")

    if len(file_content_string) >= MAX_CHARS:
        return file_content_string + f"...File \"{file_abspath}\" truncated at 10000 characters"
    else:
        return file_content_string
