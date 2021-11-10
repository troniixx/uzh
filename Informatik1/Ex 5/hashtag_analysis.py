#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):

    ALPHA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    result = {}

    for item in posts:
        for word in item.split(): #split element into singular words
            if word.startswith("#") and len(word) > 1: #if word starts with # and isnt len <= 0
                if word.replace("#", "") not in result: #check if word isnt in dict
                    result[word.replace("#", "")] = 1   #if not in dict add id with value 1
                else:
                    result[word.replace("#", "")] += 1 #if it is in list, add 1 to the value
    #print(result)
    #print("\n")

    #for key in result.copy():
    #    if key.startswith("."):
    #        del result[key]

    print(result)
    print("\n")

    #for key in result.copy():
    #    if key.startswith("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0"):
    #        del result[key]


    for key in result.copy():
        if not key[0].isalpha():
            del result[key]


    return result
# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
if __name__ == '__main__':
    posts = [
        "hi #weekend",
        "good morning #zurich #limmat", "#fuck#this",
        "spend my #weekend in #zurich", "# ", "#§",
        "#zurich <3 #", "#20appleMeDaddy!?+",
        "#.c.", "#ZURICH", "#123", "5LMAOR", "#*", "##aa"]
    
    print(analyze(posts))
