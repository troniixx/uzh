#!/usr/bin/env python3

def dict_to_lists(d):
    keys = []
    values = []
    for (k, v) in d.items():
        keys.append(k)
        values.append(v)
    return (keys, values)

