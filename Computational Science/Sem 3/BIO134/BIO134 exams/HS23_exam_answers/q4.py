#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 4

pi_poem =  'How I wish I could recollect, of circle round, '
pi_poem += 'the exact relation Arkimedes unwound.'

pi_poem = pi_poem.replace(',','')
pi_poem = pi_poem.replace('.','')

words = pi_poem.split()

beforeDecimalPoint = True
piFound = ''

for i, word in enumerate(words):
    
    wordLength = len(word)
    piFound += str(wordLength)
    print(wordLength, word + (10-wordLength)*' ' + piFound)
    
    if beforeDecimalPoint:
        print('.')
        piFound += '.'
        beforeDecimalPoint = False
        