def sum_list(numbers):

    result = 0
    length = len(numbers)

    if length == 0:
        return (0, 0)

    for element in numbers:
        if element % 2 == 0:
            result += element
        else:
            result -= element


    return ((length, result))

print(sum_list([]))
print(sum_list([2,4,7]))