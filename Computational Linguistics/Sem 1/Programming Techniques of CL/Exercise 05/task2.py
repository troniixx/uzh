"""
PCL Exercise 5
Author: PCL Tutors
University of Zurich
Student Names: <your names>

Task: Comment the code below and explain what it does.
"""

#THis function prints the sentence inside the function
#the sentence is a local variable
def function1():
    sentence = "This is a sentence."
    print(sentence)

#the global keyword makes the variable sentence global
#this means that the variable sentence is not only defined inside the function but also outside of it
def function2():
    global sentence
    sentence = "This is a different sentence."
    print(sentence)


sentence = "This is a third sentence."
function1() #this calls the function function1 and prints the sentence inside the function
print(sentence) #this prints the sentence outside of the function on line 24
function2() #this calls the function function2 and prints the sentence inside the function and changes the sentence globally
print(sentence) #this prints the sentence inside of the function2 on line 20
