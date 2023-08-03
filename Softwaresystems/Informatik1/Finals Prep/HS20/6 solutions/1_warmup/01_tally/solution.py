#!/usr/bin/env python3

def tally(costs, discounts, rebate_factor):
    # the traditional way:
    res = 0
    for c in costs:
        res += c
    for d in discounts:
        res -= d
    if res < 0:
        return 0
    return round(res * rebate_factor, 2)
    # the fast way:
    #return max(0, round((sum(costs) - sum(discounts)) * rebate_factor, 2))

