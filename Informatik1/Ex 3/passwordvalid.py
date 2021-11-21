#!/usr/bin/env python3
# "+", "-", "*", "/".
# Must contain at least 2 lower case and 2 upper case characters, 2 digits, and 2 special chars.
__author__ = "Mert Erol"
pwd = "aA00++"


def is_valid():
    special = ["+", "-", "*", "/"]
    upper = 0
    lower = 0
    digit = 0
    spam = 0
    specialdigit = 0
    # You need to change the following part of the function
    # to determine if it is a valid password.
    validity = True
    validity1 = True
    validity2 = False

    if not any(char.isdigit() for char in pwd): validity1 = False

    if not any(char.islower() for char in pwd): validity1 = False

    if not any(char.isupper() for char in pwd): validity1 = False

    if not any(char in special for char in pwd): validity1 = False

    # You don't need to change the following line.
    # return validity

    for i in range(len(pwd)):
        if pwd[i].isupper():
            upper = upper + 1

        if pwd[i].islower():
            lower = lower + 1

        if pwd[i].isdigit():
            digit = digit + 1

        if pwd[i] == "+":
            specialdigit = specialdigit + 1

        if pwd[i] == "-":
            specialdigit = specialdigit + 1

        if pwd[i] == "*":
            specialdigit = specialdigit + 1

        if pwd[i] == "/":
            specialdigit = specialdigit + 1

    if upper >= 2:
        spam = spam + 1

    if lower >= 2:
        spam = spam + 1

    if digit >= 2:
        spam = spam + 1

    if specialdigit >= 2:
        spam = spam + 1

    if spam == 4:
        validity2 = True

    if validity2 == validity1:
        validity = True
    else:
        validity = False

    # You don't need to change the following line.
    print(spam)
    print(validity2)
    print(validity1)
    print(lower, upper, specialdigit, digit)
    return validity


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.

print(is_valid())