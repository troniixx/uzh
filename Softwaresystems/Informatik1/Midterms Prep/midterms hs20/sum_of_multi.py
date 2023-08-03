# sum_of_multiplications([(1, 2), (5, 10)]) should return 52
# because (1 * 2 + 5 * 10) is 52
def sum_of_multiplications(l):
    sum = 0

    for value1, value2 in l:
        sum += value1 * value2

    return sum

if __name__ == '__main__':
    print(sum_of_multiplications([(1, 2), (5, 10)]))