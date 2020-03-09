def binary_search(list1, item):
    low = 0
    high = len(list1) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list1[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 6, 10000]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
