import numpy as np

def my_occurrences(M, x):
    l = []

    for row in M:
        l.append(np.count_nonzero(row == x))

    return l

def my_find(v, x, t):
    l = []

    for element in v:
        if element - x <= t:
            l.append(v.index(element))

    return l

if __name__ == '__main__':
    M = np.array([[1, 2, 1], [1, 2, 3], [1, 2, 3]])
    x = 1
    print(my_occurrences(M, x))

    v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 5
    t = 2
    print(my_find(v, x, t))