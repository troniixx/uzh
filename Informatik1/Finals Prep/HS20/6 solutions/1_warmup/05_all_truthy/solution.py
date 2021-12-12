#!/usr/bin/env python3

def all_truthy(values):
    # the traditional way:
    for v in values:
        if not v:
            return False
    return True
    # the fast way:
    #return all(values)

