#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 2

tens = [7, 4, 6, 0, 3, 5, 1, 4, 8, 2]
ones = [3, 1, 5, 2, 6, 2, 9, 8, 4, 1]

numbers = []
for i in range(len(tens)):
    number = 10*tens[i] + ones[i]
    numbers.append(number)
print(numbers)