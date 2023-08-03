#!/usr/bin/env python3
__author__ = "Mert Erol"
PATH = "/Users/merterol/Desktop/uzhpython/uzh/Informatik1/data process/titanic.csv"
# This signature is required for the automated grading to work.
def rundown(path):
    tuples = []
    path = PATH
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

def preprocess(records):
    cleaned = []
    surv = ["yes", "Yes", "no", "No", "Dead", "Alive", "dead", "alive", "f", "t", "T", "F"]
    cash = ["1", "2", "3"]
    name = []
    gender = ["male", "female", "Male", "Female", "F", "M"]
    age_range = str((0, 101))
    age = str(list(age_range))
    ma_kari = []
    srce_moje = []
    piqk_nonen = []
    final = []

    #get rid of tuples with empty entries
    for tuple in records:
        if not all(tuple):
            del tuple
        else:
            cleaned.append(tuple)

    piqk_nonen.append(cleaned[0])

    #get rid of tuples that dont match surv

    for tuple in cleaned:
        if tuple[0] in surv:
            ma_kari.append(tuple)
        else:
            del tuple
    #print("surv  ", ma_kari)

    #get rid of tuples that dont match cash
    for tuple in ma_kari:
        if tuple[1] in cash:
            srce_moje.append(tuple)
        else:
            del tuple
    #print("cash  ", srce_moje)

    #get rid of tuples that dont match gender
    for tuple in srce_moje:
        if tuple[3] in gender:
            piqk_nonen.append(tuple)
        else:
            del tuple
    
    #print("gender  ", piqk_nonen)
    """""
    #get rid of tuples that dont match age
    for tuple in piqk_nonen:
        if tuple[4] in age:
            final.append(tuple)
        else:
            del tuple
    """""

    return piqk_nonen

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
    ('no', '3', 'Braund Ms. Maria', 'Female', '22', ''), #remove
    ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
    ('', '3', 'Vander Planke Miss. Augusta Maria', 'female', '', ''), #remove
    ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')
    # ...
]


print(preprocess(titanic))
#print(preprocess(rundown(PATH)))
