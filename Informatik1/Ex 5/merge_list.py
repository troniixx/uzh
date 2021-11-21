#!/usr/bin/env python3
__author__ = "Mert Erol"
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

"""""
description:
merge([0, 1, 2], [5, 6, 7]) # should return [(0, 5), (1, 6), (2, 7)]
merge([2, 1, 0], [5, 6])    # should return [(2, 5), (1, 6), (0, 6)]
merge merge([2, 1], [5, 6, 7]) should return [(2, 5), (1, 6), (1, 7)]
merge([], [2, 3])           # should return []
"""""


def merge(a, b):
    mergelist = []

    #if either a or b is empty
    if not a or not b:
        return mergelist

    #case 1 (both have same number of elements)
    if len(a) == len(b):
        for i in range(len(a)):
            mergelist.append((a[i], b[i]))

    for i in a, b:
        if len(a) > len(b):
            b.append(b[-1])
        elif len(a) < len(b):
            a.append(a[-1])
    mergelist = list(zip(a, b))

    return mergelist



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
if __name__ == '__main__':
    print("a = b = ", merge([0, 1, 2], [5, 6, 7]))
    print("a > b = ", merge([2, 1, 0], [5, 6]))
    print("a < b = ", merge([2, 1], [5, 6, 7]))
    print("a empty = ", merge([], [0, 1]))
    print("b empty = ", merge([0, 1], []))

