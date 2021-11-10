#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fine_calculator(area, speed):
    areas = ["urban", "expressway", "motorway"]

    if area not in areas:
        raise ValueError("Invalid Area Value")
    
    if type(area) != str:
        raise ValueError("Invalid Area Type")

    if type(speed) != int:
        raise ValueError("Invalid Speed Type")
    elif type(speed) != float:
        raise ValueError("Invalid Speed Type")
    
    if speed < 0:
        raise ValueError("Invalid Speed Value")

    print("what")

    
    return 0

if __name__ == '__main__':
    print(fine_calculator("motorway", -3))
    """
        The speed limit for Urban areas is 50 km/h, and the fine coefficient is 1
        The speed limit for Expressway areas is 100 km/h, and the fine coefficient is 0.8
        The speed limit for Motorway areas is 120 km/h, and the fine coefficient is 0.5
    """