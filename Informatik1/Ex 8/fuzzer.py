#!/usr/bin/env python3
import random

# These variables are required for the automatic grading to work, do not change
# their names. You can change values of these variables.
min_length_global = 0
max_length_global = 5
char_start_global = 30
char_end_global = 65


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fuzzer(min_length, max_length, char_start, char_end):
    sol = ""
    r = random.randint(min_length, max_length+1)
    
    while len(sol) != r:
        x = random.randint(char_start, char_end+1)
        y = chr(x)
        sol = sol + y

    return sol


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def calculate_factorial(inp):
    if inp == None:
        return None
    
    if int(inp) > 10:
        raise ValueError("ValueError: number too large")

    pass
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def run(trials):

    # this function should make use of the other two functions
    # for the input of the fuzzer functions use the global variables
    # this is required else the automatic testing is not working
    pass

# The following line calls the function run and prints the return
# value to the Console.
if __name__ == '__main__':
    print(fuzzer(4, 10, 43, 57))
    print(run(10))

