#!/usr/bin/env python3

def calc(expression):
    op, left, right = expression.split()
    left = float(left)
    right = float(right)
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "/":
        if right == 0:
            raise ValueError
        return left / right
    if op == "*":
        return left * right