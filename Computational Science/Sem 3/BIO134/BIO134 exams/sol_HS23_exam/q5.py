#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 5

import numpy as np

f = open('densities.csv', 'r')
lines = f.readlines()
f.close()

letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

plateArray = np.zeros((4,6))

for line in lines:
    
    letter,columnAsString, valueAsString  = line.strip().split(',')
    rowIndex = letter_to_index[letter]
    columnIndex = int(columnAsString)-1
    value = float(valueAsString)
    
    plateArray[rowIndex, columnIndex] = value
        
print(plateArray)

# calculate means and count non-viable wells
wildtypeRows = plateArray[:2,:]
mutantRows = plateArray[2:,:]

# find non-viable wells using loops
nonViablesWildtype = 0
for row in wildtypeRows[:2,:]:
    for value in row:
        if value < 0.05:
            nonViablesWildtype += 1
            
# alternative to loops: find non-viable wells using boolean array indexing
nonViablesMutant = len(mutantRows[mutantRows<0.05])

print('wildtype')
print('mean density:', np.mean(wildtypeRows))
print('number of non-viable wells:', nonViablesWildtype)
print('mutant')
print('mean density:', np.mean(mutantRows))
print('number of non-viable wells:', nonViablesMutant)


