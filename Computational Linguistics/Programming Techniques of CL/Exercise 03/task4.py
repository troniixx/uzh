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
    def filtering(dune):
        filtered_dune = []
        
        for word in dune:
            if word not in stopwords:
                filtered_dune.append(word)
        
        return filtered_dune

    #c
    def frequency(dune):
        filtered_dune = filtering(dune)
        frequency = {}

        for word in filtered_dune:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
            
        return frequency

    #d
    def get_word(dune):
        return dune[0]
    
    def sorting(dune):
        freq = frequency(dune)
        sorted_frequency = sorted(freq.items(), key = get_word)
        
        return sorted_frequency
    
if __name__ == '__main__':
    print(sorting(dune))