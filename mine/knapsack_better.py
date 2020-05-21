import numpy as np

'''
------------------------------------------------
Use dynamic programming (DP) to solve 0/1 knapsack problem
Time complexity: O(nW), where n is number of items and W is capacity
------------------------------------------------
knapsack_dp(values,weights,n_items,capacity,return_all=False)
Input arguments:
  1. values: a list of numbers in either int or float, specifying the values of items
  2. weights: a list of int numbers specifying weights of items
  3. n_items: an int number indicating number of items
  4. capacity: an int number indicating the knapsack capacity
  5. return_all: whether return all info, default is False (optional)
Return:
  1. picked: a list of numbers storing the positions of selected items
  2. max_val: maximum value (optional)
------------------------------------------------
'''


def knapsack_dp(values, weights, n_items, capacity, return_all=False):
    check_inputs(values, weights, n_items, capacity)

    table = np.zeros((n_items + 1, capacity + 1), dtype=np.float32)
    keep = np.zeros((n_items + 1, capacity + 1), dtype=np.float32)

    for i in range(1, n_items + 1):
        for w in range(0, capacity + 1):
            wi = weights[i - 1]  # weight of current item
            vi = values[i - 1]  # value of current item
            if (wi <= w) and (vi + table[i - 1, w - wi] > table[i - 1, w]):
                table[i, w] = vi + table[i - 1, w - wi]
                keep[i, w] = 1
            else:
                table[i, w] = table[i - 1, w]

    picked = []
    k = capacity

    for i in range(n_items, 0, -1):
        if keep[i, k] == 1:
            picked.append(i)
            k -= weights[i - 1]

    picked.sort()
    picked = [x - 1 for x in picked]  # change to 0-index

    if return_all:
        max_val = table[n_items, capacity]
        return picked, max_val
    return picked


def check_inputs(values, weights, n_items, capacity):
    # check variable type
    assert (isinstance(values, list))
    assert (isinstance(weights, list))
    assert (isinstance(n_items, int))
    assert (isinstance(capacity, int))
    # check value type
    assert (all(isinstance(val, int) or isinstance(val, float) for val in values))
    assert (all(isinstance(val, int) for val in weights))
    # check validity of value
    assert (all(val >= 0 for val in weights))
    assert (n_items > 0)
    assert (capacity > 0)


if __name__ == '__main__':
    v = [10, 3, 9, 5, 6]
    i_weight = [3, 1, 2, 2, 1]
    count = 5
    max_count = 6
    picks = knapsack_dp(v, i_weight, count, max_count, return_all=True)
    print(picks)
