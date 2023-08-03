#!/usr/bin/env python3

import random

def lottery(values):
    draw = random.sample(range(1,51), k=len(values))
    matches = 0
    for v in values:
        if v in draw:
            matches += 1
    return draw, matches

