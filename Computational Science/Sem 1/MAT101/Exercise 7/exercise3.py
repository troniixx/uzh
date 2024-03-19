import numpy as np

#a)
a = np.ones((3, 3))

#b
b = np.eye(3)

#c
c = a+b

#d
v = np.array([7, 11, 2022])
d = np.matmul(b, v)

#e
e = np.array([
            [1, 0, 4, 4],
            [0, 1, 4, 4],
            [0, 0, 19, 0],
            [0, 0, 0, 2]
            ])

print(a, "\n")
print(b, "\n")
print(c, "\n")
print(d, "\n")
print(e)