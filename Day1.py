def sort012(arr):
    # count number of 0s, 1s, and 2s
    count0 = 0
    count1 = 0
    count2 = 0
    
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1
    
    # overwrite the array
    index = 0
    for i in range(count0):
        arr[index] = 0
        index += 1
    for i in range(count1):
        arr[index] = 1
        index += 1
    for i in range(count2):
        arr[index] = 2
        index += 1
    
    return arr


# test cases
print(sort012([0, 1, 2, 1, 0, 2, 1, 0]))
print(sort012([2, 2, 2, 2]))
print(sort012([0, 0, 0, 0]))
print(sort012([1, 1, 1, 1]))
print(sort012([2, 0, 1]))
print(sort012([]))
