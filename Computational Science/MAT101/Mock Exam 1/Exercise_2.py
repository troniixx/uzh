# -*- coding: utf-8 -*-
# Author: Mert Erol, 20-915-245

import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from time import perf_counter_ns as timer

# a)
def partial_sum(n: int) -> float:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Error: the argument should be a natural number")

    res = 0
    for num in range(n+1):
        res += ((-1)**num) / (num+1)
        
    return res

# b)
def convergence_vector(v: list) -> list:
    return [partial_sum(n) for n in v]

def convergence_vector_opt(v: list) -> list:
    if not all(isinstance(num, int) and num >= 0 for num in v):  # Ensure v is a list of natural numbers
        raise ValueError("Error: all elements of the list should be natural numbers")

    max_val = max(v)
    
    
    

def time_comparison(v: list) -> None:
    time_conv = timer()
    result_conv = convergence_vector(v)
    end_time_conv = timer()
    
    time_conv_opt = timer()
    result_conv_opt = convergence_vector_opt(v)
    end_time_conv_opt = timer()
    
    print("Time for convergence_vector: ", end_time_conv - time_conv)
    print("Result for convergence_vector: ", result_conv)
    print("Time for convergence_vector_opt: ", end_time_conv_opt - time_conv_opt)
    print("Result for convergence_vector_opt: ", result_conv_opt)
    
    return None
if __name__ == "__main__":
    v = [100, 200]
    time_comparison(v)