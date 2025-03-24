import matplotlib.pyplot as plt
import numpy as np
from sys import argv

def sum_throws(data):
    sums = []

    with open(data, 'r') as f:
        for line in f:
            nums = list(map(int, line.strip().split(' ')))
            sums.append(sum(nums))

    return sums

def summer(data):
    sums = sum_throws(data)

    plt.histogram(sums[:100], bins=range(3, 19), density=True)
    plt.title('Sum of 3 dice rolls')
    plt.xlabel('Sum')
    plt.ylabel('Frequency')
    plt.show()

def histo(data):
    sums = sum_throws(data)

    plt.histogram(sums, bins=range(3, 19), density=True)
    plt.title('Sum of 3 dice rolls')
    plt.xlabel('Sum')
    plt.ylabel('Frequency')
    plt.show()

def histo_with_error(data):
    pass

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: python throwing_dice.py <txt file>')
        exit(1)

    data = argv[1]
    summer(data)
    histo(data)
    histo_with_error(data)
