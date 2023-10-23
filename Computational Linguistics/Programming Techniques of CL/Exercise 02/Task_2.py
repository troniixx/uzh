"""
PCL & PFL Exercise 2, Task 2
Author: PCL & PFL Tutors
University of Zurich
Student Names: Mert Erol
"""


# ----- Your code goes here ----- #
print("Enter a value for a: ")
#a = int(input())
a = float(input())
print("Enter a value for b: ")
#b = int(input())
b = float(input())

x = 12*(a**2)*b-9*(b**3)*a
y = (x*(b+a))/(0.4*b+0.3*(a**2))

print("Value of x: ", x)
print("Value of y: ", y)

"""
Part 2:
If either x or y can be calculated as an integer, 
then the result will be an integer if the input is convered into an integer.
If the input is a float, then the result will always be a float.
"""
