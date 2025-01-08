#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 1

seq = 'TAATTTCTGACNATGGCGTCAATGGTACTCGCGNNGAG'


# using flag
print('\nusing flag')
flag = True
for letter in seq:
    if letter == 'N':
        flag = False
    if flag:
        print(letter)
 
    
# using break
print('\nusing break')
for letter in seq:
    if letter == 'N':
        break
    print(letter)
    
    
# using partition  
print('\nusing partition')
parts = seq.partition('N')
for n in parts[0]:
    print(n)
    
    