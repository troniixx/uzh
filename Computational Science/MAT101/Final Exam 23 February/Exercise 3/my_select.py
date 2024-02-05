import numpy as np
import math

def my_select(d, w, y):
    out = []

    for element in w:
        if abs(element - y) > d:
            out.append(element)

    return out

def my_columns(A, y):
    l = []

    