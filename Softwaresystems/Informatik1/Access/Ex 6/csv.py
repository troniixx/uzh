#!/usr/bin/env python3
__author__ = "Mert Erol"
# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def read_csv(path):
    tuples = []
    file = open(path, "r")
    
    for line in file:
        if line:
            tuples.append(tuple(line.strip().split(",")))
        else:
            del line

    while ("",) in tuples:
        tuples.remove(("",))

    file.close()
    return tuples

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
if __name__ == '__main__':
    print(read_csv("/Users/merterol/Desktop/uzhpython/uzh/Informatik1/Ex 6/task1.csv"))
    print(read_csv("public/example.csv"))  