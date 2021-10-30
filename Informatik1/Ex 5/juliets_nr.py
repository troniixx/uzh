#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    # This function accepts a string n for juliets number where one digit is missing.
    # and should return a list of all whatsapp numbers that might belong to juliet 
    possible_nrs_for_juliet = []
    x = 10

    for i in range(len(n)):
        for y in range((x)):
            y = str(y)
            number_complete = n[:i] + y + n[i:]

            if i == max(range(len(n))):
                number_complete = n[:i+1] + y

            possible_nrs_for_juliet.append(number_complete)

    list1 = set(wa_nrs)
    intersect = list1.intersection(possible_nrs_for_juliet)
    intersect_list = list(intersect)
    n = intersect_list

    return n
    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))
