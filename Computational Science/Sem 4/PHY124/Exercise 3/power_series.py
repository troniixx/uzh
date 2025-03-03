from math import factorial, pi

def one(n):
    return (-1)**n

def two(n):
    return 2*n + 1

def three(x, n):
    return x**n

def four(x):
    return factorial(x)

print(one(3))
print(two(3))
print(three(2, 3))
print(four(3))

def sin(x):
    return sum([one(n) * three(x, two(n)) / four(two(n)) for n in range(10)])

print(round(sin(-5*pi / 13), 8))