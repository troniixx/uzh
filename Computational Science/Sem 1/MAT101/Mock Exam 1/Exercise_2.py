# -*- coding: utf-8 -*-
# Author: Mert Erol, 20-915-245

import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from time import perf_counter_ns as timer
import math

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
    if not all(isinstance(num, int) and num >= 0 for num in v):  # Ensure v is a list of natural numbers
        raise ValueError("Error: all elements of the list should be natural numbers")
    
    return [partial_sum(n) for n in v]

# c)
def convergence_vector_opt(v: list) -> list:
    if not all(isinstance(num, int) and num >= 0 for num in v):  # Ensure v is a list of natural numbers
        raise ValueError("Error: all elements of the list should be natural numbers")

    max_val = max(v)
    partial_sums = [0] * (max_val + 1)

    res, sign = 0, 1
    for num in range(1, max_val + 2):
        res += sign / num
        partial_sums[num - 1] = res
        sign *= -1
        
    return [partial_sums[n] for n in v]

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

def plotter(v: list) -> None:
    res_opt = convergence_vector_opt(v)
    
    plt.figure()
    plt.scatter(v, res_opt, label = "Partial Sums")
    plt.xscale("log")
    plt.axhline(math.log(2), color='r', linestyle='dashed', label='log(2)')
    plt.title("Partial Sums vs log(2)")
    plt.xlabel("n")
    plt.legend()
    plt.grid(True)
    
    plt.savefig("/Users/merterol/uzh/Computational Science/MAT101/Mock Exam 1/plot_convergence.pdf")
    #plt.show()

if __name__ == "__main__":
    v = [100, 200]
    n = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    time_comparison(v)
    plotter(n)