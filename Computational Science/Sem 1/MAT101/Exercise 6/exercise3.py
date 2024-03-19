import numpy as np

array_31 = np.array([-10, 0, 30, 2, 20, 0])
print("a:")
print(f"max = {np.where(array_31 == np.max(array_31))}")
print(f"min = {np.where(array_31 == np.min(array_31))}")
print(f"zeros = {np.where(array_31 == 0)}")

array_32 = np.random.uniform(0, 1, 1000)

array_33 = np.sort(array_31)
print("b: ", array_33)

np.savetxt("sorted_33.txt", array_33)
array_34 = np.loadtxt("sorted_33.txt")

array_35 = np.append(array_34, array_32)
print("e: ", array_35)

np.savetxt("sorted_and_original_arrays.txt", (array_35))