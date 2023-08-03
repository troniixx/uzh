#You are completely free to change this variables to check your algorithm.
__author__ = "Mert Erol"
num1 = 6
num2 = 28

def isFriendlyPair():
    sum1 = 0
    sum2 = 0
    validity = True
    if type(num1) != int:
        return "Invalid"

    if type(num2) != int:
        return "Invalid"

    if num1 == num2:
        return "Invalid"

    if num1 <= 0:
        return "Invalid"

    if num2 <= 0:
        return "Invalid"

    for i in range(1,num1):
        if(num1 % i == 0):
            sum1 = sum1 + i

    for i in range(1,num2):
        if(num2 % i == 0):
            sum2 = sum2 + i

    if(sum1/sum2 == num1/ num2):

        return True
    else:
        return False

print(isFriendlyPair())