def f(num):
    if not isinstance(num, int) or num < 0:
        raise TypeError("num must be a positive integer")
    else:
        if num % 2 == 0:
            return num // 2
        else:
            return 3 * num + 1

def collatz(num):
    if not isinstance(num, int) or num < 0:
        raise TypeError("num must be a positive integer")
    
    result = []
    
    while num != 1:
        result.append(num)
        num = f(num)

    result.append(1)
    return result

#TODO longest collatz
def longest_collatz():
    result = 0
    for num in range(1, 10000):
        if len(collatz(num)) > len(collatz(result)):
            result = num
    return result


if __name__ == "__main__":
    print(longest_collatz())