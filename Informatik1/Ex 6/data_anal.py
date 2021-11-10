#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gender_class_rates(dataset):
    # implement this function
    # the function might have other useful parameters, explore `help(round)`
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []

    for data in range(len(dataset[1])):
        if "" not in dataset[1][data] and len(dataset[1][data]) == 6:
            #collecting number of females in each class
            if dataset[1][data][3] == "female":
                if dataset[1][data][1] == 1:
                    list_4.append(1)
                elif dataset[1][data][1] == 2:
                    list_5.append(2)
                else:
                    list_6.append(3)
            #collecting number of males in each class
            else:
                if dataset[1][data][1] == 1:
                    list_1.append(1)
                elif dataset[1][data][1] == 2:
                    list_2.append(2)
                else:
                    list_3.append(3)
    
    #number of all passangers
    all = len(list_1) + len(list_2) + len(list_3) + len(list_4) + len(list_5) + len(list_6)

    #female ratio
    out1 = [round(len(list_1)/all * 100, 1), round(len(list_2)/all * 100, 1), round(len(list_3)/all * 100, 1)]

    for i in range(len(out1)):
        if out1[i] == 0.0:
            out1[i] = None
    #male ratio
    out2 = [round(len(list_4)/all * 100, 1), round(len(list_5)/all * 100, 1), round(len(list_6)/all * 100, 1)]

    for j in range(len(out2)):
        if out2[j] == 0.0:
            out2[j] = None
    

    return(tuple(out1), tuple(out2))


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!


# Investigate the 'titanic.csv' file before you attempt a submission.
# You might want to download the file to your machine and open it with the functions that you have written in Task 1+2.
# The following example is not complete.
if __name__ == '__main__':
    print(gender_class_rates((
        ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
        [
            (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
            'female', 38, 71.2833),
            (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
            # ...
        ]
    )))
