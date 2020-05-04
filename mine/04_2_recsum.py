def simple_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


def rec_sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + rec_sum(arr[1:])


print(simple_sum([1, 2, 3, 4]))
print(rec_sum([1, 2, 3, 4]))
