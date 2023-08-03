#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def tally(costs, discounts, rebate_factor):
    sum_c = 0
    sum_d = 0

    for cost in costs:
        sum_c += cost

    for discount in discounts:
        sum_d += discount

    res = (sum_c - sum_d) * rebate_factor

    if res < 0:
        return 0
    else: return round(res, 2)

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
# ((10+24) - (3+4+3)) * 0.3
assert(tally([10,24], [3,4,3], 0.30) == 7.20)
# if the result would be negative, 0 is returned instead
assert(tally([10], [20], 0.1) == 0)