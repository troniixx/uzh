"""
PCL & PFL Exercise 2, Task 3
Author: PCL & PFL Tutors
University of Zurich
Student Names: Mert Erol, Ishana Rana
"""


# ----- Your code goes here ----- #

food = input("Enter your favorite food? ")
country = input("Enter your favourite country: ")

if len(food) > 7:
    if len(country) == 5:
        print(f"It seems like your {food.upper()} is popular in beautiful {country.upper()}")
    else:
        print(f"It seems like your {food.upper()} is popular in {country.upper()}")
else:
    if len(country) == 5:
        print(f"It seems like your {food} is popular in beautiful {country}")
    else:
        print(f"It seems like your {food} is popular in {country}")
