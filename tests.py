from functions.get_files_info import get_files_info

test_result_1 = get_files_info("calculator", ".")
print(f"{test_result_1}")

test_result_2 = get_files_info("calculator", "pkg")
print(f"{test_result_2}")

test_result_3 = get_files_info("calculator", "/bin")
print(f"{test_result_3}")

test_result_4 = get_files_info("calculator", "../")
print(f"{test_result_4}")