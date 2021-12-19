def reverse(list):
    if len(list) < 2:
        return list
    return [list[-1]] + reverse(list[:-1])

assert reverse([]) == []
assert reverse([2]) == [2]
assert reverse([2, 6, 5]) == [5, 6, 2]