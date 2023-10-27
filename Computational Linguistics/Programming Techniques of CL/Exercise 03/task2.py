#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s):
# date:

# TASK 2

# TODO your implementation here

def isPalindrome():
    flag = True
    #get the input
    string = input("Please enter a word! ").lower()
    
    #check if the input is a word
    if not string.isalpha():
        print(ValueError("Please enter a valid word!"))
        return
    
    #check if the word is a palindrome by comparing the nth first and nth last letters
    for char in range (0, len(string)//2):
        if string[char] != string[-char-1]:
            flag = False
            break
    
    #print the result
    if flag:
        print("This word is a palindrome!")
    else:
        print("This word is not a palindrome!")
        
if __name__ == "__main__":
    isPalindrome()