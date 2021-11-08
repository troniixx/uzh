#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gender_class_rates(dataset):
    # implement this function
    # the function might have other useful parameters, explore `help(round)`
    final = []
    male_values = ["Male", "male", "M", "m"]
    female_values = ["Female", "female", "F", "f"]
    male_first = []
    female_first = []
    male_second = []
    female_second = []
    male_third = []
    female_third = []

    for element in dataset:
        if element[1] == 1 and element[3] in male_values:
            element.append(male_first)
        elif element[1] == 1 and element[3] in female_values:
            element.append(female_first)
        elif element[1] == 2 and element[3] in male_values:
            element.append(male_second)
        elif element[1] == 2 and element[3] in female_values:
            element.append(female_second)
        elif element[1] == 3 and element[3] in male_values:
            element.append(male_third)
        elif element[1] == 3 and element[3] in female_values:
            element.append(female_third)
        else:
            continue


    round(1.2345)
    pass


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!


# Investigate the 'titanic.csv' file before you attempt a submission.
# You might want to download the file to your machine and open it with the functions that you have written in Task 1+2.
# The following example is not complete.
print(gender_class_rates((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
        'female', 38, 71.2833),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
        # ...
    ]
)))
