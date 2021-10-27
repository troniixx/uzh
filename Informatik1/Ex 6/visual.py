#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def visualize(records):
    pass


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
