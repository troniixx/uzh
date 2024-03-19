import numpy as np

array11 = np.array([1, 2, 3])
array12 = np.array([1.68, 2.71, 3.14])

#b
print("b: ", array11 + array12)

#c
print("c: ", array11 * array12)

#d
print("d: ", array11 / 5)

#e
print("e: ", array11 ** 2)

#f
print("f: ", np.concatenate((array11, array12)))

#g
print("g: ", np.concatenate((array11, array12))[1:-1])