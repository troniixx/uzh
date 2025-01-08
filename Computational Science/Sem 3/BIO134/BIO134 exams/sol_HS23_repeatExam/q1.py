#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 1

genotypes = [1, 4, 2, 1, 3, 4, 3, 4, 1, 4, 3, 2, 4, 4, 2]

smallerThanFour = 0
for num in genotypes:
    if num < 4:
        smallerThanFour += 1

print(smallerThanFour)
print(smallerThanFour/len(genotypes))