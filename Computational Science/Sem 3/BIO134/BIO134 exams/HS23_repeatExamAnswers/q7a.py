#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 7

import numpy as np

# small example from question text #################
samples = 3
species = 4
data    = [1,4,15,1,3,2,6]
indices = [0,2,0,0,2,1,2]
indptr  = [0,2,3,5,7]

# final dataset to be used as input #################
samples = 10
species = 9
data    = [1, 4, 6, 1, 2, 2, 2, 1, 5, 1, 11, 3, 11, 2, 9, 7, 5, 11, 75, 1, 6, 103, 8, 11, 51, 13, 41, 44, 52, 16, 2, 2, 2, 1, 1, 1]
indices = [3, 4, 5, 6, 7, 2, 6, 9, 2, 9, 0, 6, 0, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 1, 7, 1, 7, 9]
indptr  = [0, 5, 8, 10, 12, 20, 30, 31, 33, 36]


# task 1: create full matrix ########################
fullMatrix = np.zeros((samples, species), dtype=int)

for column in range(len(indptr) - 1):
    
    indStart = indptr[column]
    indEnd = indptr[column + 1]
    
    for i in range(indStart, indEnd):
        row = indices[i]
        fullMatrix[row, column] = data[i]

print('task1: create full matrix')
print(fullMatrix)

# task 2a: richness ##################################
print('\ntask 2a')

highestRichness = -1 
highestRichnessSample = None
lowestRichness = species + 1
lowestRichnessSample = None

for sample in range(samples):
    counter = 0
    for specie in range(species):
        if fullMatrix[sample, specie] > 0:
            counter += 1
    if counter > highestRichness:
        highestRichness = counter
        highestRichnessSample = sample + 1
    if counter < lowestRichness:
        lowestRichness = counter
        lowestRichnessSample = sample + 1

print ("highest: sample {}, richness {}".format(highestRichnessSample, highestRichness))
print ("lowest: sample {}, richness {}".format(lowestRichnessSample, lowestRichness))

# task 2b: Shannon diversity index H' #################
print('\ntask 2b')

highestShannon = 0
highestShannonSample = None
lowestShannon = np.log(species) # this is specialized knowledge
lowestShannonSample = None

for sample in range(samples):
    totalCounter = 0
    shannon = 0
    for specie in range(species):
        totalCounter += fullMatrix[sample, specie]
    for specie in range(species):
        if fullMatrix[sample,specie] > 0:
            fraction = fullMatrix[sample,specie] / float(totalCounter)
            shannon += fraction * np.log(fraction)
    shannon *= -1.0

    if shannon > highestShannon:
        highestShannon = shannon
        highestShannonSample = sample + 1
    if shannon < lowestShannon:
        lowestShannon = shannon
        lowestShannonSample = sample + 1

print("highest: sample {}, H' {:.4f}".format(highestShannonSample, highestShannon))
print("lowest: sample {}, H' {:.4f}".format(lowestShannonSample, lowestShannon))