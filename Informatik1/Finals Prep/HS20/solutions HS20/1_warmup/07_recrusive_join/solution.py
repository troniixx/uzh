#!/usr/bin/env python3

def recursive_join(delim, values):
    if len(values) == 1:
        return values[0]
    return values[0] + delim + recursive_join(delim, values[1:])

