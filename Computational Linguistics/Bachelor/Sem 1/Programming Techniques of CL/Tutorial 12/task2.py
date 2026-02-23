def func(num):
    if num < 0 and num%2 != 0:
        return "Negative Odd"
    elif num > 0 and num%2 == 0:
        return "Positive Even"
    return "sad :("

print(func(5))
print(func(-5))
print(func(4))
print(func(-4))
print(func(0))