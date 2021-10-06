import math

# You are completely free to change this variables to check your algorithm.
num1 = 5
num2 = 28


# Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    sum1 = 0
    sum2 = 0

    for i in range(1, num1):
        if num1 % i == 0:
            sum1 = sum1 + i

    for i in range(1, num2):
        if num2 % i == 0:
            sum2 = sum2 + i

    if num1 / num2 == sum1 / sum2:
        return True
    else:
        return False


# This line prints your method's return so that you can check your output.
print(isFriendlyPair())
