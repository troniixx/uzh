#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 3

import numpy as np 
np.random.seed(1)


def guessing(guess1, guess2):
    counter = 0
    while True:
        counter += 1
        toss = np.random.randint(1,7)
        print(toss)
        if toss == guess1:
            return 1, toss, counter
        if toss == guess2:
            return 2, toss, counter

w, n, a = guessing(3,4) # winner, number, attempt
print('Player {} won! {} was rolled with the {}. roll.'.format(w, n, a))
