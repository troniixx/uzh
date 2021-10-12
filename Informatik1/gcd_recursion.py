#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):

    # implement this function
    return abs(a)

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a, b):

    # handle negative numbers
    if a < 0:
        a = absolute_value(a)

    if b < 0:
        b = absolute_value(b)

    # constraints
    if a == 0:
        if (a == 0) and (b == 0):
            return None
        return absolute_value(b)
    elif b == 0:
        if (a == 0) and (b == 0):
            return None
        return absolute_value(a)

    # euclid
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")
