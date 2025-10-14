import os 

def write_file(working_directory, file_path, content):
    my_file_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))
    # print(f"my_directory: {my_directory}")
    # If the absolute path to the directory is outside the working_directory, return a string error message:
    dir_abspath = os.path.abspath(working_directory)
    # print(f"dir_abspath: {dir_abspath}")
    if not my_file_path.startswith(dir_abspath):
        return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    # If the directory argument is not a directory, again, return an error string:
    if not os.path.isdir(working_directory):
        return(f'Error: "{working_directory}" is not a directory')

    if not os.path.exists(my_file_path):
        try:
            with open(my_file_path, "w") as f:
                f.write(content)
            print(f'Successfully wrote to "{my_file_path}" ({len(content)} characters written)')
        except:
            print(f"Error: can't create file {my_file_path}")
    else:
        try:
            with open(my_file_path, "w") as f:
                f.write(content)
            print(f'Successfully wrote to "{my_file_path}" ({len(content)} characters written)')
        except:
            print(f"Error: can't write to {my_file_path}")

        