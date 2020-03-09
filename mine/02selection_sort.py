def find_smallest(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(1, len(arr)):
        if arr[1] < smallest:
            smallest = arr[i]
            smallest_ind = i
    return smallest_ind


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([1, 3, 2, 100, 23, 2444, 33]))
