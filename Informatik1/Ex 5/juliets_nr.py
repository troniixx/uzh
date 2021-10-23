""""
your job in this task is to help Romeo by writing a program that produces all possibilities of phone numbers
and provides him a list of possble numbers that are linked on Whatsapp. For this you may adhere to the following specification:

Valid numbers have 10 digits in total and start with 07

get_possible_nrs(n) accepts a number string n where one digit is missing
n may be assumed to start with 07 and then contain 7 further digits (in total 9, i.e. one missing digit).

get_possible_nrs(n) returns a list of whatsapp number strings that might belong to juliet.

A number that may belong to juliet contains exactly one digit more than n (10 digits).

The single missing digit may be assumed to be at any index after the starting 07 within n.

Make sure your returned list does not contain duplicates.

wa_nrs is a list of numbers that are registered with Whatsapp.

Compare your generated numbers with the numbers in wa_nrs to return only those from your function which exist in Whatsapp.
"""

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
    all_possible_numbers = []
    possible_nrs_for_juliet = []
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    #constraints
    if len(n) < 2:
        return False

    if len(n) > 10:
        return False

    for char in range(len(n)):
        if n[char] not in digits:
            return False

    #get the number of digits missing from number
    x = 10 - len(n)

    for i in range(x):
        for d in range(9):
            n += str(d)
            if len(n) == 10:
                all_possible_numbers.append(n)
    

    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))

#testing
print(get_possible_nrs("075"))
print()
