def find_missing_number(arr):
    n = len(arr) + 1  # because one number is missing
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum


# Test Cases
print(find_missing_number([1, 2, 4, 5]))       # 3
print(find_missing_number([2, 3, 4, 5]))       # 1
print(find_missing_number([1, 2, 3, 4]))       # 5
print(find_missing_number([1]))                # 2
print(find_missing_number(list(range(1, 1000000))))  # 1000000
