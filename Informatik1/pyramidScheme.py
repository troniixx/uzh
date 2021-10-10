#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 4

# build a string
def build_string_pyramid():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""

    if h == 0:
        s = ""

        # untere hälfte
    for i in range(0, h):
        c = 1
        print(c, end=" ")
        for j in range(h - i - 1, 0, -1):
            print('*', end=" ")
            c = c + 1
            print(c, end=" ")
        print("\n")

    return s

    # Enter your code here
    # use nested loops and the range() function
    """
    for i in range(1, h + 1):
        for j in range(1, i + 1):
            print(str(j)+"*", end = " ")
        print(" ")

    for i in range(1, h + 1):
        for j in range(h - i, 0, -1):
            print(str(j)+"*", end=" ")
        print(" ")
"""

"""
#obere hälfte
    for i in range(0, h):
        e = 1
        print(e, end = " ")
        for j in range(1, h + i + 1):
            print("*", end = " ")
            e = e + 1
            print(e, end = " ")
        print("\n")
"""


    # You don't need to change the following line.
    # It simply returns the string created above

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())
