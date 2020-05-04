def max_(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = max_(lst[1:])
        # return lst[0] if lst[0] > sub_max else sub_max
        if lst[0] > sub_max:
            return lst[0]
        else:
            return sub_max


print(max_([100, 1, 2, 3, 4]))
