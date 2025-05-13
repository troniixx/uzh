import numpy as np

"""
      0────1
     /│   /│
    3─┼──2 │       ← top face
    │ 4──┼─5
    │/   │/
    7────6          ← bottom face
"""

# Total nodes in cube
n = 8

# Initialize conductance matrix
# Creates an 8×8 conductance matrix (Y), initialized with zeros.
Y = np.zeros((n, n))

# Define resistor connections (with resistance values)
edges = [
    (0, 1, 0.63),  # special resistor R1
    (1, 2, 1), (2, 3, 1), (3, 0, 1),  # top face
    (4, 5, 1), (5, 6, 1), (6, 7, 1), (7, 4, 1),  # bottom face
    (0, 4, 1), (1, 5, 1), (2, 6, 1), (3, 7, 1)  # vertical edges
]
"""
resistor as a tuple:
(node1, node2, resistance).
"""

# Build conductance matrix (Y)
for u, v, r in edges:
    g = 1 / r  # conductance
    Y[u, u] += g
    Y[v, v] += g
    Y[u, v] -= g
    Y[v, u] -= g
    
""" This loop fills in the conductance matrix Y, using:
1/R for each resistor.
Each resistor affects four entries in the matrix."""


# Current vector: +1 A into node 0 (A), -1 A out of node 6 (B)
I = np.zeros(n)
I[0] = 1
I[6] = -1
"""
This defines the current injection vector:
1 A into node 0 (A)
1 A out of node 6 (B)
Other nodes have no external current source"""


# Ground node 7 by removing its row and column
ground = 7
Y_reduced = np.delete(np.delete(Y, ground, axis=0), ground, axis=1)
I_reduced = np.delete(I, ground)
"""
To solve the equations, we need to fix one voltage (set it to 0 V). This is called "grounding".
Here, node 7 is grounded
Remove its row and column from the matrix Y
Remove its entry from the current vector I
Now the system has full rank and can be solved."""


# Solve for voltages
V = np.linalg.solve(Y_reduced, I_reduced)

# Reconstruct full voltage vector, with 0 V at ground
V_full = np.insert(V, ground, 0)

# Calculate voltage difference between A (0) and B (6)
R_eq = V_full[0] - V_full[6]
print(f"Equivalent resistance: {R_eq:.3f} ohms")
