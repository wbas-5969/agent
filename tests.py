from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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

get_files_content = get_file_content("calculator", "main.py")
print(f"file content: {get_files_content}")

get_files_content = get_file_content("calculator", "pkg/calculator.py")
print(f"file content: {get_files_content}")

get_files_content = get_file_content("calculator", "/bin/cat")
print(f"file content: {get_files_content}")

get_files_content = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"file content: {get_files_content}")

