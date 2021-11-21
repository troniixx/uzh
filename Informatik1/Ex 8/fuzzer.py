#!/usr/bin/env python3
import random
__author__ = "Mert Erol"
# These variables are required for the automatic grading to work, do not change
# their names. You can change values of these variables.
min_length_global = 1
max_length_global = 10
char_start_global = 45
char_end_global = 57


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fuzzer(min_length, max_length, char_start, char_end):
    string = ""
    for a in range(random.randint(min_length,max_length)):
        string += chr(random.randint(char_start,char_end))
        list = []
        for i in string:
            list.append(i)
        random.shuffle(list)
        string = ''.join(list)
    return string


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def calculate_factorial(inp):
    fact = 1
    if inp == None:
        return None
    try:
        int(inp)
    except:
        raise TypeError("TypeError: string")
    else:
        integer = int(inp)
    if integer < 0:
        raise ValueError("ValueError: number negative")
    elif integer > 10:
        raise ValueError("ValueError: number too large")
    else:
        for i in range(1, integer+1):
            fact = fact*i
        return fact



def run(trials):
    rtrn_list = []
    if isinstance(trials, int) and trials > 0:
        for runs in range(trials):
            try:
                calculate_factorial(fuzzer(min_length_global, max_length_global, char_start_global, char_end_global))
            except TypeError:
                success = 1
                strng = "Other error"
            except ValueError as err:
                success = 1
                strng =str(err)
            else:
                success = 0
                strng = ""


            rtrn_list.append((success,strng))
        return rtrn_list
    else:
        return []


    # this function should make use of the other two functions
    # for the input of the fuzzer functions use the global variables
    # this is required else the automatic testing is not working


# The following line calls the function run and prints the return
# value to the Console.
print(run(5))
