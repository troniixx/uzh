"""
PCL & PFL Exercise 2, Task 5a
Author: PCL & PFL Tutors
University of Zurich
Student Names: Mert Erol, Ishana Rana
"""

# ----- You can ignore the following lines of code for now ----- #

from random import randint
n = randint(1, 20)  # <- this is the number of sheeps 'n' you should use

# ----- Your code goes here ----- #
print(n)
counter = 1
print("The computer is counting sheep to fall asleep!")
while(counter < n+1):
    print(counter, "sheep")
    counter += 1
    
print("z.. z.. z..")
print(f"The computer fell asleep after counting {n} sheep. Sweet dreams little machine!")
