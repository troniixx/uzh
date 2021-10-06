import math

# You are completely free to change this variables to check your algorithm.
num1 = 5
num2 = 28


# Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    sum1 = 1 + num1  # sum of divisor of num1
    sum2 = 1 + num2  # sum of divisor of num2
    i = 2
    j = 2
    # finding divisor
    while i <= math.sqrt(num1):
        if num1 % i == 0:
            if num1 // i == i:
                sum1 += i

            else:
                sum1 += i + num1 // i

        i = i + 1

    while j <= math.sqrt(num2):
        if num2 % j == 0:
            if num2 // j == j:
                sum2 += j

            else:
                sum2 += j + num2 // j

        j = j + 1
    if sum1 / num1 == sum2 / num2:
        return True
    else:
        return False


# This line prints your method's return so that you can check your output.
print(isFriendlyPair())
