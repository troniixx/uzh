#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 6

import numpy as np
#
binary = np.zeros(shape=(6,8),dtype=int) 
binary[0,7] = 1
binary[5,3] = 1
binary[3,1:4] = 1 
#

output = np.zeros(binary.shape, dtype=int) 

(nRows, nColumns) = binary.shape

for row in range(nRows):
    for column in range(nColumns):
        for rowRange in (-1, 0, 1):
            for colRange in (-1, 0, 1):
                if not (rowRange, colRange) == (0, 0):
                    neighborRow = row + rowRange
                    neighborCol = column + colRange
                    if neighborRow >= 0 and neighborRow < nRows:
                        if neighborCol >= 0 and neighborCol < nColumns:
                            if binary[neighborRow, neighborCol] == 1:
                                output[row, column] += 1

print(output)




