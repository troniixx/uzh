#!/usr/bin/env python3

def are_anagrams(a, b):
    # the traditional way:
    aa = []
    bb = []
    for c in a:
        if c.isalpha():
            aa.append(c.lower())
    for c in b:
        if c.isalpha():
            bb.append(c.lower())
    aa.sort()
    bb.sort()
    return aa == bb

    # the fast way:
    #a = sorted([c.lower() for c in a if c.isalpha()])
    #b = sorted([c.lower() for c in b if c.isalpha()])
    #return a == b


