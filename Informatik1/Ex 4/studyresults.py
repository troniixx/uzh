#!/usr/bin/env python3
__author__ = "Mert Erol"
import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):
        return None

    list_me = []


    file = open(path, "r")
    
    for line in file: 
        f = line.replace(" ","")
        f = f.replace("\n", "")
        f_split = f.split(":")
        if len(f_split) == 2:
            if f_split[1] == "":
                del f_split[1]
            else:
                list_me.append(f_split[1])
    
    if len(list_me) == 0:
        file.close()
        return 0.0
    
    avg = 0.0
    for x in list_me:
        avg = avg + float(x)
    if avg > 0.0:
        file.close()
        return avg/len(list_me)
    else:
        file.close()
        return None 

    
    

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("/Users/merterol/Desktop/uzhpython/uzh/Informatik1/Ex 4/my_grades.txt"))