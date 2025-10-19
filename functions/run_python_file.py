import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="runs the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file_path to the file",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="arguments to the python script",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    my_file_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))
    # print(f"my_directory: {my_directory}")
    # If the absolute path to the directory is outside the working_directory, return a string error message:
    dir_abspath = os.path.abspath(working_directory)
    # print(f"dir_abspath: {dir_abspath}")
    if not my_file_path.startswith(dir_abspath):
        return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

    # If the directory argument is not a directory, again, return an error string:
    if not os.path.isdir(working_directory):
        return(f'Error: "{working_directory}" is not a directory')
    
    # if file doesn't exist, error
    if not os.path.exists(my_file_path):
        print(f'Error: File "{file_path}" not found.')
    
    if not my_file_path.endswith('.py'):
        print(f'Error: "{file_path}" is not a Python file.')

    try:
        completed_process = subprocess.run([my_file_path, *args], cwd=working_directory,timeout=30)
        return_code = completed_process.returncode
        stdout_text = completed_process.stdout
        stderr_text = completed_process.stderr

        if stdout_text == '':
            return_string = "No output produced"
        else:
            return_string = f"STDOUT: {stdout_text}\nSTDERR: {stderr_text}\n"
            if not return_code != 0:
                return_string = return_string + f"Process executed with code {return_code}"
    except Exception as e:
        print(f"could not run lol")
        return_string = f"Error: executing Python file: {e}"
    
    return return_string