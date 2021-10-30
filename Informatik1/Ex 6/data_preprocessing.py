#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def preprocess(records):
    pass


# The following part calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

# Investigate the 'titanic.csv' file before you attempt a submission.
# You might want to download the file to your machine and open it with the function that you have written in Task 1.
# The following example is not complete.

titanic = [
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
    ('no', '3', 'Braund Ms. Maria', 'Female', '22', ''),
    ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
    ('', '3', 'Vander Planke Miss. Augusta Maria', 'female', '', ''),
    ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')
    # ...
]

print(preprocess(titanic))
