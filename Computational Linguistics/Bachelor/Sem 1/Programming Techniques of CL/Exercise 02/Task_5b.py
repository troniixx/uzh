"""
PCL & PFL Exercise 2, Task 5b
Author: PCL & PFL Tutors
University of Zurich
Student Names: Mert Erol, Ishana Rana
"""

# ----- You can ignore the following lines of code for now ----- #

from random import randint
n = randint(1, 20)  # <- this is the number of sheeps 'n' you should use

# ----- Your code goes here ----- #
import random
import time

# Generate a random number of sheep to count
n = random.randint(1, 20)  # You can adjust the range as needed
count = 0

print("The computer is counting sheep to fall asleep!")

while count < n:
    count += 1
    print(f"{count} sheep")

# Falling asleep simulation (optional)
time.sleep(2)
print("z.. " * 4)
time.sleep(2)
print(f"Your computer fell asleep after counting {count} sheep. Sweet dreams little machine!")


# Answers:

"""Similarities and differences:
The way the random int is generated is the same.
The way the sheep are counted in the loop is the same. 

Printing the lines with the z is way different and it also uses the time library for some reason
The end message uses the counter instead of the n variable.
"""


"""Explanation for 2.:
The idea behind it is the same but the output has small differences, because the code is not exactly the same.
"""
