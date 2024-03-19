# -*- coding: utf-8 -*-
# Author: Mert Erol, 20-915-245

import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt

def degree(P: list) -> float:
    return len(P)-1

def eval_polynomial(P: list, x: float) -> float:
    return sum(coef * (x**i) for i, coef in enumerate(P))

def polynomial_derivative(P: list) -> list:
    return [coef * (i + 1) for i, coef in enumerate(P[1:])]

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.degree = degree(coeffs)
    
    def derivative(self):
        derived_coeffs = polynomial_derivative(self.coeffs)
        return Polynomial(derived_coeffs)
    
    def __add__(self, other):
        # find the length of the longer polynomial
        max_length = max(len(self.coeffs), len(other.coeffs))
        
        # extend both coefficient lists to the length of the longer one, using 0 for missing coefficients
        coeffs1 = self.coeffs + [0] * (max_length - len(self.coeffs))
        coeffs2 = other.coeffs + [0] * (max_length - len(other.coeffs))
        
        # sum the coefficients
        new_coeffs = [a + b for a, b in zip(coeffs1, coeffs2)]
        
        # remove trailing zeros (if any) to avoid incorrect degree
        while new_coeffs and new_coeffs[-1] == 0:
            new_coeffs.pop()
        
        return Polynomial(new_coeffs)

    # __str__ method to print the polynomial in a nice way, without this i just the the address of the object in memory
    def __str__(self):
        terms = [f"{coef}x^{i}" for i, coef in enumerate(self.coeffs) if coef]
        return " + ".join(terms).replace("x^0", "").replace("x^1", "x").replace(" + -", " - ").strip()


if __name__ == "__main__":
    P_one = [1, 0, 2]
    P_two = [2, -6, 2, -1]
    P_three = [0, 0, 0, 5]
    x_value = 4
    
    # a) degree of the polynomial
    print("Degree of the polynomial:", degree(P_three))

    # b) evaluation of the polynomial at x_value
    print("P({}) =".format(x_value), eval_polynomial(P_three, x_value))

    # c) derivative of the polynomial
    print("Derivative coefficients:", polynomial_derivative(P_three))

    # d) using the class Polynomial
    poly = Polynomial(P_three)
    poly_derivative = poly.derivative()
    print("Polynomial:", poly)
    print("Derivative Polynomial:", poly_derivative)

    # addition of two polynomials
    poly_sum = poly + poly_derivative
    print("Sum of Polynomial and its Derivative:", poly_sum)
