#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 6

import numpy as np

binary = np.zeros(shape=(6,8),dtype=int) 
binary[0,7] = 1
binary[5,3] = 1
binary[3,1:4] = 1  

new = 0 * binary
new[:-1,:] += binary[1:,:]
new[1:,:] += binary[:-1,:]
new[:,1:] += binary[:,:-1]
new[:,:-1] += binary[:,1:]
new[1:,1:] += binary[:-1,:-1]
new[1:,:-1] += binary[:-1,1:]
new[:-1,1:] += binary[1:,:-1]
new[:-1,:-1] += binary[1:,1:]
print(new)
