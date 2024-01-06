#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Clair Chaos wrote a program in order to test whether you have the magical power to correctly guess the number that a dice rolls.
# Actually, the program lets you guess infinitely until you predict the correct number.
# But your chances are always 1/6 to predict the rolled number.
# Every non-integer is silently ignored and the user is prompted
# So, everyone is a bit of a magician in the end...
# Unfortuately, Clair Chaos mixed up all lines and lost the indentation. Can you please help her to reconstruct the program.
# IMPORTANT: Please write a short comment BEFORE EACH LINE that explains what the next line does.

### YOUR Python comments and code start here ###
# import the random module to generate random sample
import random

#start while loop that runs until the correct number is guessed
while True:
    #get user input and convert it to integer
    try:
        g = int(input("Guess which number the dice rolled: "))            
    except Exception:
        continue # cathcing the exception and continue the loop --> this is to make sure that the script does not crash if the user enters a non-integer
    else:
        dice = [1, 2, 3, 4, 5, 6] # numbers of a 6 sided dice
        r = random.sample(dice, 1) # randomly sample one number from the dice
        if r[0] == g: # check if the randomly sampled number is equal to the user input
            print(f"Amazing! The dice indeed rolled a {g}! You are a 🧙‍! ") # congrats message
            break # break the loop and terminate
        else: # if the user input is not equal to the randomly sampled number
            print("You know nothing, Jon Snow...") # print this message

### YOUR Python comments and code end here ###
