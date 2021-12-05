#!/usr/bin/env python3
# add imports, if necessary
from exchange_rates import EXCHANGE_RATES as er

def convert(amount, from_currency, to_currency):
    
    if from_currency not in er or to_currency not in er:
        raise Warning("invalid currency")
    if not isinstance(amount, (float, int)):
        raise Warning("invalid amount")
    if amount < 0: raise Warning("negative amount")

    if from_currency == to_currency:
        return amount
    else:
        for i in er:
            if i == from_currency:
                try: rate = er[from_currency][to_currency]
                except KeyError: continue
            
            elif i == to_currency:
                try: rate = 1 / er[to_currency][from_currency]
                except KeyError: continue
    
    return amount * rate
