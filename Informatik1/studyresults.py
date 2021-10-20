#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):

    #what to do if file dodesnt exist
    if not os.path.exists(path):
        return None

    list_me = []
    list_us = []

    f = open("/Users/merterol/Desktop/uzhpython/uzh/Informatik1/my_grades.txt")

    #get all values after : from txt file
    lines = f.readlines()
    for line in lines:
        x = line.find(":")
        list_me.append(line[x+1:])

    #get rid of newlines
    for e in list_me:
        list_us.append(e.strip())

    #removing emtpy strings
    while "" in list_us:
        list_us.remove("")

    #getting rid of non-grades
    new_list = []
    for e in list_us:
        if e in ("1.0", "1", "1.25", "1.5", "1.75", "2.0", "2", "2.25", "2.5", "2.75", "3.0", "3", "3.25", "3.5", "3.75", 
        "4.0", "4", "4.25", "4.5", "4.75", "5.0", "5", "5.25", "5.5", "5.75", "6.0", "6"):
            new_list.append(e)
    list_us = new_list
    
    if len(list_us) == 0:
        avg = 0.0
    else:
        test_list = [float(i) for i in list_us]
        list_us = test_list
        avg = sum(list_us)/len(list_us)
        
    """""
    used this for testing
    print(list_me)
    print(list_us)
    """""

    #closing file
    f.close()

    return avg



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("/Users/merterol/Desktop/uzhpython/uzh/Informatik1/my_grades.txt"))
