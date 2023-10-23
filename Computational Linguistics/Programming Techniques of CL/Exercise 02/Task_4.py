"""
PCL & PFL Exercise 2, Task 4
Author: PCL & PFL Tutors
University of Zurich
Student Names: Mert Erol, 
"""


# ----- Your code goes here ----- #
noun = input("Please enter a german noun: ")
der = ["smus", "ner", "ich", "ist"]
die = ["heit", "keit", "ung", "schaft"]
das = ["chen", "tum","lein", "ium"]

if noun.endswith(tuple(der)):
    print(f"Der {noun}")
elif noun.endswith(tuple(die)):
    print(f"Die {noun}")
elif noun.endswith(tuple(das)):
    print(f"Das {noun}")
else:
    print("Gender cannot be determined.")
