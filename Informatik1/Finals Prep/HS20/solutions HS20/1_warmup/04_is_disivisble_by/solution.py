#!/usr/bin/env python3

def is_divisible_by(x, numbers):
    if not numbers or 0 in numbers:
        raise ValueError
    for n in numbers:
        if x % n != 0:
            return False
    return True

