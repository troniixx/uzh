import numpy as np
def simple_circuit():
    M = np.array([[2, -1, -1, 0],
                [-1, 3, -1, -1],
                [-1, -1, 3, -1],
                [0, -1, -1, 2]])

    b = np.array([1, 0, 0, -1])
    x = np.linalg.solve(M, b)

    print("Simple Circuit")
    for i in range(len(x)):
        print(f"x{i+1} = {x[i]:.2f}")


def solve_resistor_network(r1=0.63):
    """
    Solve for the equivalent resistance between points A and B in the given network.
    
    The network is a 3D cube-like structure with:
    - R1 = 0.63 ohms (the red resistor on top)
    - All other resistors = 1 ohm each (the purple resistors)
    
    Method: Using nodal analysis with Kirchhoff's current law
    """
    # Number the nodes: A=0, B=7, and interior nodes 1-6
    num_nodes = 8
    
    # Create conductance matrix (inverse of resistance)
    # G[i,j] = G[j,i] = -1/R for nodes connected by resistance R
    # G[i,i] = sum of all conductances connected to node i
    G = np.zeros((num_nodes, num_nodes))
    
    # Define connections with their resistances
    # Format: (node1, node2, resistance)
    connections = [
        (0, 1, r1),    # A to top-front-left (R1)
        (0, 2, 1.0),   # A to top-back-left
        (1, 3, 1.0),   # top-front-left to top-front-right
        (2, 3, 1.0),   # top-back-left to top-back-right
        (1, 4, 1.0),   # top-front-left to bottom-front-left
        (2, 5, 1.0),   # top-back-left to bottom-back-left
        (3, 6, 1.0),   # top-front-right to bottom-front-right
        (4, 5, 1.0),   # bottom-front-left to bottom-back-left
        (4, 6, 1.0),   # bottom-front-left to bottom-front-right
        (5, 7, 1.0),   # bottom-back-left to B
        (6, 7, 1.0),   # bottom-front-right to B
        (5, 6, 1.0),   # bottom-back-left to bottom-front-right
        (3, 7, 1.0),   # top-back-right to B
    ]
    
    # Fill conductance matrix
    for i, j, r in connections:
        g = 1.0 / r  # Conductance = 1/Resistance
        G[i, j] -= g
        G[j, i] -= g
        G[i, i] += g
        G[j, j] += g
    
    # Apply test voltage: 1V between A and B
    V_A = 1.0
    V_B = 0.0
    
    # Create right-hand side of Ax = b
    b = np.zeros(num_nodes)
    b[0] = G[0, :].sum() * V_A  # Current at node A
    b[7] = G[7, :].sum() * V_B  # Current at node B
    
    # Remove rows and columns for nodes with known voltages (A and B)
    G_reduced = G[1:7, 1:7]
    b_reduced = b[1:7] - G[1:7, 0] * V_A - G[1:7, 7] * V_B
    
    # Solve for unknown voltages
    V_unknown = np.linalg.solve(G_reduced, b_reduced)
    
    # Reconstruct full voltage vector
    V = np.zeros(num_nodes)
    V[0] = V_A
    V[1:7] = V_unknown
    V[7] = V_B
    
    # Calculate current from A to B
    I_A = sum(G[0, j] * (V[0] - V[j]) for j in range(num_nodes))
    
    # Calculate equivalent resistance
    R_eq = (V_A - V_B) / I_A
    
    return R_eq

if __name__ == "__main__":
    simple_circuit()
    r_eq = solve_resistor_network(0.63)

    # Format the result to three decimal places
    formatted_result = "{:.3f}".format(r_eq)
    
    print(f"The equivalent resistance between A and B is {formatted_result} Ω")