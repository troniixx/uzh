# author: Mert Erol, 20-915-245, merol
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

SAND = "/Users/merterol/uzh/Computational Science/Sem 3/PHY231/Exercise 4/sand.txt"

cov_matrix = np.array([1.068, -0-302], [-0.302, 0.118])
m = ufloat(16.1, 1.0)
q = ufloat(-2.61, 0.34)

#plot the data
