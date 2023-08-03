def find_max(list):
    max = 0

    for i in list:
        if max is None or i > max:
            max = i
    
    return max

numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]

print(find_max(numbers))