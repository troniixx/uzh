#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 0

# build a string
def build_string_pyramid():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""

    for i in range(h):
        for j in range(i + 1):
            if j == max(range(i + 1)):
                s += str(j + 1)
            else:
                s += str(j + 1) + "*"
        s += "\n"

    for i in range(h - 1, 0, -1):
        for j in range(1, i + 1):
            if j == max(range(1, i + 1)):
                s += str(j)
            else:
                s += str(j) + "*"
        s += "\n"

    return s



    # Enter your code here
    # use nested loops and the range() function

    # You don't need to change the following line.
    # It simply returns the string created above

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())
