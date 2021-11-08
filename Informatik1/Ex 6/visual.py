#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def visualize(records):
    pclass_1 = 0
    pclass_1_alive = 0
    pclass_2 = 0
    pclass_2_alive = 0
    pclass_3 = 0
    pclass_3_alive = 0

    dataset = records[1]

    for p in dataset:
        pclass = p[1]
        alive = p[0]

        #first class counter
        if pclass == 1:
            pclass_1 += 1
            if alive == True:
                pclass_1_alive += 1
        #second class counter
        elif pclass == 2:
            pclass_2 += 1
            if alive == True:
                pclass_2_alive += 1
        #third class counter
        elif pclass == 3:
            pclass_3 += 1
            if alive == True:
                pclass_3_alive += 1

    #percentage of passengers in each class
    totpas = len(dataset)
    tot_1 = round((pclass_1/totpas * 100), 1)
    tot_2 = round((pclass_2/totpas * 100), 1)
    tot_3 = round((pclass_3/totpas * 100), 1)

    #percentage of each passanger that survived in each class
    surv_1 = round((pclass_1_alive/pclass_1 * 100), 1)
    surv_2 = round((pclass_2_alive/pclass_2 * 100), 1)
    surv_3 = round((pclass_3_alive/pclass_3 * 100), 1)

    #building the visual step by step
    string = "== 1st Class ==\n"
    string += "Total |" + (round(tot_1/5)) * "*" + str((20- round(tot_1/5))* " ") + "| " + str(tot_1) + "%\n"
    string += "Alive |" + (round(surv_1/5)) * "*" + str((20-round(surv_1/5)) * " ") + "| " + str(surv_1) + "%\n"
    string += "== 2nd Class ==\n"
    string += "Total |" + (round(tot_2/5)) * "*" + str((20- round(tot_2/5))* " ") + "| " + str(tot_2) + "%\n"
    string += "Alive |" + (round(surv_2/5)) * "*" + str((20-round(surv_2/5)) * " ") + "| " + str(surv_2) + "%\n"
    string += "== 3rd Class ==\n"
    string += "Total |" + (round(tot_3/5)) * "*" + str((20- round(tot_3/5))* " ") + "| " + str(tot_3) + "%\n"
    string += "Alive |" + (round(surv_3/5)) * "*" + str((20-round(surv_3/5)) * " ") + "| " + str(surv_3) + "%\n"

    return string

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
