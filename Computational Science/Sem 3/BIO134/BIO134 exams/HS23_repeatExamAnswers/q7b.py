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
    
    fullMatrix[indices[indStart:indEnd], column] = data[indStart:indEnd]

print('task1: create full matrix')
print(fullMatrix)

# task 2a: richness ##################################
print('\ntask 2a')

richness = np.sum(fullMatrix>0, 1)
samplesArr = np.linspace(1, samples, samples,dtype=int)

highestRichness = np.max(richness)
highestRichnessSample = samplesArr[richness==highestRichness][0]
lowestRichness = np.min(richness)
lowestRichnessSample = samplesArr[richness==lowestRichness][0]

print ("highest: sample {}, richness {}".format(highestRichnessSample, highestRichness))
print ("lowest: sample {}, richness {}".format(lowestRichnessSample, lowestRichness))

# task 2b: Shannon diversity index H' #################
print('\ntask 2b')
shannon = []
relativeAbundances = fullMatrix*0.

for i, row in enumerate(fullMatrix):
    relativeAbundances[i,:] = fullMatrix[i,:]/np.sum(fullMatrix, 1)[i]
    nonZeroRelAbundances = relativeAbundances[i,relativeAbundances[i]>0]
    shannon.append((-np.sum(nonZeroRelAbundances*np.log(nonZeroRelAbundances)), i + 1))

shannon.sort()

highestShannon = shannon[-1][0]
highestShannonSample = shannon[-1][1]
lowestShannon = shannon[0][0]
lowestShannonSample = shannon[0][1]

print("highest: sample {}, H' {:.4f}".format(highestShannonSample, highestShannon))
print("lowest: sample {}, H' {:.4f}".format(lowestShannonSample, lowestShannon))