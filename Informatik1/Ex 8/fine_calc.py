#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fine_calculator(area, speed):
    areas = ["urban", "expressway", "motorway"]

    if type(area) != str:
        raise ValueError("Invalid Area Type")
    elif area not in areas:
        raise ValueError("Invalid Area Value")
    elif type(speed) != int:
        if type(speed) != float:
            raise ValueError("Invalid Speed Type")
    elif speed < 0:
        raise ValueError("Invalid Speed Value")

    fine = 0

    if area == "urban":
        if speed > 50:
            fine = ((((100/50*speed)-100)**2) * 1)
        else: return 0
    elif area == "expressway":
        if speed > 100:
            fine = ((((100/100*speed)-100)**2) * 0.8)
        else: return 0
    elif area == "motorway":
        if speed > 120:
            fine = ((((100/120*speed)-100)**2) * 0.5)
        else: return 0


    
    return round(fine)

if __name__ == '__main__':
    print(fine_calculator("motorway", 180))
    print(fine_calculator("expressway", 140))
    print(fine_calculator("urban", 80))

    #print(fine_calculator("boom", 130)) 
    #print(fine_calculator(1, 130))
    #print(fine_calculator("motorway", "130"))
    #print(fine_calculator("motorway", -12))
