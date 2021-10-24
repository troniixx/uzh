#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):

    result = {}

    for item in posts:
        for word in item.split(): #split element into singular words
            if word.startswith("#") and len(word) > 1: #if word starts with # and isnt len <= 0
                if word.replace("#", "") not in result: #check if word isnt in dict
                    result[word.replace("#", "")] = 1   #if not in dict add id with value 1
                else:
                    result[word.replace("#", "")] += 1 #if it is in list, add 1 to the value

    return result
# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3 #",
    ".#c.", "#ZURICH"]

print(analyze(posts))
