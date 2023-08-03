#!/usr/bin/env python3

def find_both_ways(text, word):
    text = text.lower()
    word = word.lower()
    if word in text:
        return (True, 1)
    if word in text[::-1]: # or if word in ''.join(reversed(text)):
        return (True, -1)
    return (False, 0)

