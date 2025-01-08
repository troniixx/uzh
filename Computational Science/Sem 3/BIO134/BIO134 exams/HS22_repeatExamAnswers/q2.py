#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 2

original = ['my', 'care', 'is', 'loss', 'of', 'care', 'by', 'old', 'care', 'done'] 

unique = []
for word in original:
    if word not in unique:
        unique.append(word)
        
print(unique)