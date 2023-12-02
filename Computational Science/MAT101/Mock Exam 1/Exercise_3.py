# -*- coding: utf-8 -*-
# Author: Mert Erol, 20-915-245

import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt

def degree(P: list, x: int) -> float:
    pass

def eval_polynomial(P: list, x: float) -> float:
    pass

def polynominal_derivative(P: list) -> list:
    pass

class Polynomial:
    
    def __init__(self, d: int, coefs: list):
        self.d = d
        self.coefs = coefs
        
    def derivative(self, d, coefs):
        if d < 1:
            return [1]
        
        res = []
        
        for coef in self.coefs:
            res.append(coef-1)
            
    def __add__(self, other):
        res = []
        for idx, coef in enumerate(self.coefs):
            res.append(coef + other.coefs[idx])