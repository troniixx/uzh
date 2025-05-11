import numpy as np
from scipy.sparse import lil_matrix, eye
from scipy.sparse.linalg import spsolve

def solve_resistor_grid(N):
    """
    Solve the resistor grid problem for an N x N grid.
    Returns the equivalent resistance between (0,0) and (N-1,N-1).
    """
    total_nodes = N * N
    
    # Create a sparse matrix for efficiency
    Rinv = lil_matrix((total_nodes, total_nodes))
    
    # Fill the matrix according to Kirchhoff's current law
    for i in range(N):
        for j in range(N):
            node = i * N + j
            # Diagonal element counts the number of neighbors
            Rinv[node, node] = 4
            
            # Connect to neighbors (if they exist)
            if i > 0:
                Rinv[node, node - N] = -1  # up
            if i < N - 1:
                Rinv[node, node + N] = -1  # down
            if j > 0:
                Rinv[node, node - 1] = -1  # left
            if j < N - 1:
                Rinv[node, node + 1] = -1  # right
    
    # Convert to compressed sparse column format for efficient solving
    Rinv = Rinv.tocsc()
    
    # Set up the current vector: 1A in, -1A out
    current = np.zeros(total_nodes)
    current[0] = 1          # (0,0) node: current enters
    current[-1] = -1        # (N-1,N-1) node: current exits
    
    # Solve the linear system to get voltages
    voltage = spsolve(Rinv, current)
    
    # The resistance is the voltage difference between the two points
    resistance = voltage[0] - voltage[-1]
    
    return resistance

# Test for various grid sizes
grid_sizes = [2, 5, 10, 20, 50]
for N in grid_sizes:
    R = solve_resistor_grid(N)
    print(f"Grid size {N}x{N}: Equivalent resistance = {R:.6f} ohms")