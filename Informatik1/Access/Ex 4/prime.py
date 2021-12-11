#!/usr/bin/env python3
__author__ = "Mert Erol"
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def is_prime(n):
    # author: Mert Erol
    # implement this function
    # flag var to check for prime
    check = False

    # list to help find smallest divisor
    list1 = []

    # base cases n = 1  and n < 1
    if n == 1:
        return "1 is the multiplicative identity"

    if n <= 0:
        return "Invalid"

    if n > 1:
        # check if prime or not
        for i in range(2, n):
            if (n % i) == 0:
                check = True
                break

        # get smallest divisor of n
        for j in range(2, n + 1):
            if (n % j) == 0:
                list1.append(j)
            list1.sort()

    # get b value for return string
    y = int(list1[0])
    z = n // y

    # is n prime or not
    if check:
        return f"{n} is not a prime number ({y} * {z} = {n})"
    else:
        return f"{n} is prime"


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
q = int(input("Enter a number: "))
print(is_prime(q))
