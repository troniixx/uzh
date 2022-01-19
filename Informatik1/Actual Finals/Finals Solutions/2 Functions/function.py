#!/usr/bin/env python3

def gregorian_to_ifc(day, month, leap=False):
    month = month - 1
    day = day - 1
    days_per_month = [31, 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]
    if leap: days_per_month[1] = 29

    day_number = 0
    for m in range(month):
        day_number += days_per_month[m]
    day_number += day

    if day_number in [364, 365]:
        return "Year Day"

    ifc_month = day_number // 28
    ifc_day = day_number % 28

    return ifc_day+1, ifc_month+1
