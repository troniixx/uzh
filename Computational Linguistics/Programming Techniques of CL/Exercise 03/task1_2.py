#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Mert Erol
# date:27.10.23

# TASK 1.2

# TODO your implementation here

def task():

    neg_count = 0
    pos_list = []
    neg_list = []
    
    while neg_count < 6:
        
        num = input("Enter a number: ")

        if num.isalpha():
            print(ValueError("Please enter a valid number!"))
            continue
        
        num = int(num)
        
        if num < 0:
            neg_count += 1
            neg_list.append(num)
        else:
            pos_list.append(num)
            
    print("Positive numbers: ", pos_list)
    print("Negative numbers: ", neg_list)     
        
if __name__ == "__main__":
    task()  