#!/usr/bin/env python3

def intersperse(s, l):
    res = s[0]
    delim = 0
    for c in s[1:]:
        res += l[delim % len(l)]
        res += c
        delim += 1
    return res
