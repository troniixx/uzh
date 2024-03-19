import numpy as np

array_21 = np.arange(0,4,1)
print("a: ", array_21)

array_22 = np.linspace(0,1,4)
print("b: ", array_22)

print("c: ", np.linalg.norm(array_22))
print("d: ", np.dot(array_21, array_22))
print("e: ", np.outer(array_21, array_22))
