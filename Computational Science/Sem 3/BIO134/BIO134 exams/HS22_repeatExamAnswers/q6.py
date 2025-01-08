#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 6

motif = 'ACAGTCAGT'

f = open('sequence.txt')
lines = f.readlines()
f.close()

sequence = ''
for line in lines[1:]:
    sequence += line.strip()
    
for startPos in range(0, len(sequence)-len(motif)+1):
    
    matchScore = 0
    currentFragment = sequence[startPos:startPos+len(motif)]
    matchingFragment = ''
    
    for j in range(len(currentFragment)):
        if motif[j] == currentFragment[j].upper():
            matchScore += 1
            matchingFragment += currentFragment[j].upper()      
        else:
            matchingFragment += currentFragment[j].lower()

    if matchScore >= 7:      
        print(matchingFragment, matchScore, startPos)
        
