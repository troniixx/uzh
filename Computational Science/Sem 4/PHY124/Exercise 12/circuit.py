import numpy as np

M = np.array([[2, -1, -1, 0],
            [-1, 3, -1, -1],
            [-1, -1, 3, -1],
            [0, -1, -1, 2]])

b = np.array([1, 0, 0, -1])
x = np.linalg.solve(M, b)

print("Simple Circuit")
for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.2f}")

print("Resistor Cube")

R1 = 0.63
R = 1.0

M2 = np.zeros((8, 8))

M2[0, 1] = M2[1, 0] = 1 / R1  # R1
M2[0, 2] = M2[2, 0] = 1 / R    # Top left diagonal
M2[1, 3] = M2[3, 1] = 1 / R    # Top right diagonal
M2[2, 3] = M2[3, 2] = 1 / R    # Middle horizontal
M2[2, 4] = M2[4, 2] = 1 / R    # Middle left
M2[3, 5] = M2[5, 3] = 1 / R    # Middle right
M2[4, 5] = M2[5, 4] = 1 / R    # Bottom horizontal
M2[4, 6] = M2[6, 4] = 1 / R    # Bottom left diagonal
M2[5, 7] = M2[7, 5] = 1 / R    # Bottom right diagonal
M2[6, 7] = M2[7, 6] = 1 / R    # Bottom connection

degree_matrix = np.diag(np.sum(M2, axis=1))
Laplacian_matrix = degree_matrix - M2

b = np.zeros(8)
b[0] = 1
b[7] = -1

L_reduced = Laplacian_matrix[:-1, :-1]
b_reduced = b[:-1]

v = np.linalg.solve(L_reduced, b_reduced)
I = (v[0] - 0) * (1/ R)
R = 1 / I
print(f"Resistance of the cube: {R:.3f} Ohm")