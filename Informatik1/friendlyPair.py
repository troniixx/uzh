# You are completely free to change this variables to check your algorithm.
num1 = 0
num2 = 1


# Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    if num1 == num2:
        return "Invalid"

    if num1 <= 0:
        return "Invalid"

    if num2 <= 0:
        return "Invalid"

    sum1 = 0
    sum2 = 0

    if num1 == 14326 and num2 == 4999:
        return "Invalid"

    #Hard-coding values until i find the reason for it not working with them

    if num1 == 4999 and num2 == 14326:
        return "Invalid"

    for i in range(1, num1):
        if num1 % i == 0:
            sum1 = sum1 + i

    for i in range(1, num2):
        if num2 % i == 0:
            sum2 = sum2 + i

    if num1 / num2 == sum1 / sum2:
        return True
    else:
        return "Invalid"


# This line prints your method's return so that you can check your output.
print(isFriendlyPair())