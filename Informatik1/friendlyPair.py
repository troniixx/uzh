import math
# You are completely free to change this variables to check your algorithm.
num1 = 14326
num2 = 0


# Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    if num1 == num2:
        return "Invalid"

    if num1 <= 0:
        return "Invalid"

    if num2 <= 0:
        return "Invalid"

    sum1 = 1 + num1  # sum of divisor of n
    sum2 = 1 + num2 # sum of divisor of m
    i = 2
    j = 2
    # finding divisor
    while i <= math.sqrt(num1):
        if num1 % i == i:
            if num1 // i == i:
                sum1 += i

            else:
                sum1 += i + num1 // i

        i = i + 1

    while j <= math.sqrt(num2):
        if num2 % j == j:
            if num2 // j == j:
                sum2 += j

            else:
                sum2 += j + sum2 // j

        j = j + 1
    if num1 / num2 == sum1 / sum2:
        return True
    else:
        return False


# This line prints your method's return so that you can check your output.
print(isFriendlyPair())
