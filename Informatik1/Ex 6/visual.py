#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def visualize(records):
    first = []
    second = []
    third = []
    alive_values = ["Yes", "yes", "Survived", "survived", "True", "true", "Survived=alive", "Alive", "alive", "T", "t"]
    alive_first = 0
    alive_second = 0
    alive_third = 0
    number_of_stars = 0
    
    for element in records[1]:
        if element[1] == 1:
            first.append(element)
        elif element[1] == 2:
            second.append(element)
        elif element[1] == 3:
            third.append(element)
        else:
            continue

    #calculate
    for tuple in first:
        if tuple[0] in alive_values:
            alive_first += 1
    
    for tuple in second:
        if tuple[0] in alive_values:
            alive_second += 1

    for tuple in second:
        if tuple[0] in alive_values:
            alive_third += 1
    
    #visual for first class
    print("== 1st Class ==\n")
    print("Total |", "\n")
    print("Alive |", "\n")

    #visual for second class
    print("== 2nd Class ==\n")
    print("Total |", "\n")
    print("Alive |", "\n")

    #visual for third class
    print("== 3rd Class ==\n")
    print("Total |", "\n")
    print("Alive |", "\n")

    print(first, "\n", second, "\n", third)

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(visualize((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
        'female', 38, 71.2833),
        (True, 2, 'Flunky Mr Hazelnut', 'female', 18, 51.2),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
    ]
)))
