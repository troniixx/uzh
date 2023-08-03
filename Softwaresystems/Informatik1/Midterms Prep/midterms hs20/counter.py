# count_positive_even_numbers([-2, -1, 2, 1, 4, 6, 8], 5) should return 2
# because among the first 5 numbers of the list, 2 and 4 are positive and even
def count_positive_even_numbers(numbers, n):
    counter = 0
    for i in range(0, n):
        if numbers[i] > 0 and numbers[i] % 2 == 0:
            counter += 1

    return counter

if __name__ == '__main__':
    print(count_positive_even_numbers([-2, -1, 2, 1, 4, 6, 8], 5))
