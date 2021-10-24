def compute_max_diff(numbers):
    
    
    absolute_list = []
    find_max = []

    if len(numbers) == 0:
        return 0

    if len(numbers) == 0:
        return 0

    for element in numbers:
        absolute_list.append(abs(element))

    for element in range(len(absolute_list)-1):
        if absolute_list[element] > absolute_list[element+1]:
            find_max.append(absolute_list[element] - absolute_list[element+1])
        else:
            find_max.append(absolute_list[element+1] - absolute_list[element])

    print(absolute_list)
    print(find_max)

    return max(find_max)


print(compute_max_diff([-1, 2, -3]))
print(compute_max_diff([2, 7, 5, 14, 12, 14]))
    