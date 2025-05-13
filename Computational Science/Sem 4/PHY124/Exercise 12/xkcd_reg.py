import numpy as np

def calculate_grid_resistance_numpy(N):
    # Calculate the total number of nodes in the NxN grid
    total_nodes = N * N
    
    # Initialize the conductance matrix A (NxN grid has N^2 nodes)
    # Each node is represented by a row/column in this matrix
    A = np.zeros((total_nodes, total_nodes))
    
    # Fill the conductance matrix based on the grid structure
    for i in range(N):
        for j in range(N):
            # Calculate the linear index for the current (i, j) node
            node = i * N + j
            
            # Set the main diagonal (self-conductance)
            # Each node connects to up to 4 neighbors
            A[node, node] = 4
            
            # Connect the node to its vertical and horizontal neighbors
            
            # Up neighbor (above the current row)
            if i > 0:
                A[node, node - N] = -1  # Connection to the node above
            
            # Down neighbor (below the current row)
            if i < N - 1:
                A[node, node + N] = -1  # Connection to the node below
            
            # Left neighbor (previous column)
            if j > 0:
                A[node, node - 1] = -1  # Connection to the node to the left
            
            # Right neighbor (next column)
            if j < N - 1:
                A[node, node + 1] = -1  # Connection to the node to the right
    
    # Set up the current vector
    # We inject 1A of current at the (0,0) node and extract 1A at the (N-1,N-1) node
    b = np.zeros(total_nodes)
    b[0] = 1    # Current enters the top-left node
    b[-1] = -1  # Current exits the bottom-right node
    
    # Solve the linear system A * v = b
    # This gives us the node voltages
    v = np.linalg.solve(A, b)
    
    # The equivalent resistance is simply the voltage difference between
    # the current entry and exit points (since I = 1A)
    resistance = v[0] - v[-1]
    
    return resistance

# Calculate the equivalent resistance for various grid sizes
for N in [2, 5, 10, 20, 50, 100]:
    R = calculate_grid_resistance_numpy(N)
    print(f"Grid size {N}x{N}: Equivalent resistance = {R:.6f} ohms")
