#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Mert Erol
# date: 29.10.23

# TASK 4

import sys
import nltk
from nltk.corpus import stopwords

stopwords = set(stopwords.words("english"))  # use this set for removing the stopwords

# take a look at the stopwords by printing them (and print the type – so you see it really is a set): 
#print (stopwords)
#print(type(stopwords))

# TODO your implementation here

with open("/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Exercise 03/dune.txt") as dune:
    #a
    dune = dune.read().lower().rsplit()
    
    #b
    filtered_dune = []
    
    for word in dune:
        if word not in stopwords:
            filtered_dune.append(word)

    #c
    frequency = {}
    
    for word in filtered_dune:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            

    #d
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=False)
    print(sorted_frequency)