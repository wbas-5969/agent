from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

# test_result_1 = get_files_info("calculator", ".")
# print(f"{test_result_1}")

# test_result_2 = get_files_info("calculator", "pkg")
# print(f"{test_result_2}")

# test_result_3 = get_files_info("calculator", "/bin")
# print(f"{test_result_3}")

# test_result_4 = get_files_info("calculator", "../")
# # print(f"{test_result_4}")

# get_files_content = get_file_content("./", "get_file_content.py")
# # print(f"file content: {get_files_content}")

# get_files_content = get_file_content("calculator", "lorem.txt")
# print(f"file content: {get_files_content}")

# get_files_content = get_file_content("calculator", "main.py")
# print(f"file content: {get_files_content}")

# get_files_content = get_file_content("calculator", "pkg/calculator.py")
# print(f"file content: {get_files_content}")

# get_files_content = get_file_content("calculator", "/bin/cat")
# print(f"file content: {get_files_content}")

# get_files_content = get_file_content("calculator", "pkg/does_not_exist.py")
# print(f"file content: {get_files_content}")
# my_result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print( my_result)
# my_result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print( my_result)
# my_result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print( my_result)

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))
print(run_python_file("calculator", "lorem.txt"))