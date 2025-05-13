import numpy as np
import matplotlib.pyplot as plt

# Load the initial data for the Gliese 876 system
# The file is expected to have columns for:
# Mass, x-position, y-position, x-velocity, y-velocity
df = np.loadtxt("/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 4/PHY124/Exercise 10/gliese876ini.txt")

# Extract mass, position, and velocity data from the file
M = df[:, 0]      # Masses of the bodies
X = df[:, 1]      # Initial x-positions
Y = df[:, 2]      # Initial y-positions
V_x = df[:, 3]    # Initial x-velocities
V_y = df[:, 4]    # Initial y-velocities

# Stack the position and velocity components into 2D arrays
positions = np.stack((X, Y), axis=1)  # Shape (N, 2)
velocities = np.stack((V_x, V_y), axis=1)  # Shape (N, 2)

def leapfrog(masses, positions, velocities, dt, n_steps):
    # Initialize an array to store the trajectories
    # Shape (n_steps, N, 2), where N is the number of bodies
    N = len(masses)
    traj = np.zeros((n_steps, N, 2))
    traj[0] = positions.copy()  # Store the initial positions

    # Calculate the initial accelerations based on the current positions
    acc = compute_accelerations(positions, masses)

    # Update the velocities for the first half-step
    velocities += 0.5 * dt * acc

    # Main simulation loop for the leapfrog method
    for step in range(1, n_steps):
        # Full-step position update using the half-step velocities
        positions += dt * velocities

        # Recompute the accelerations with the updated positions
        acc = compute_accelerations(positions, masses)

        # Full-step velocity update with the new accelerations
        velocities += dt * acc

        # Store the updated positions in the trajectory array
        traj[step] = positions.copy()

    return traj

def compute_accelerations(positions, masses):
    # Calculate accelerations due to gravitational interactions
    N = len(masses)
    accelerations = np.zeros_like(positions)  # Shape (N, 2) for 2D positions

    # Nested loops to compute pairwise gravitational interactions
    for i in range(N):
        for j in range(N):
            if i != j:
                # Vector pointing from body i to body j
                r = positions[j] - positions[i]
                
                # Distance between the two bodies
                dist = np.linalg.norm(r)
                
                # Gravitational acceleration contribution
                # G is assumed to be 1 for simplicity
                accelerations[i] += masses[j] * r / dist**3
    
    return accelerations

# Simulation parameters
dt = 1000  # Time step in seconds, should be small enough for stability
n_steps = 20000  # Number of time steps for the simulation

# Run the simulation to get the trajectory of each body
trajectory = leapfrog(M, positions, velocities, dt, n_steps)

# Plot the resulting orbits
plt.figure(figsize=(8, 8))
for i in range(len(M)):
    plt.plot(trajectory[:, i, 0], trajectory[:, i, 1], label=f"Body {i}")
plt.gca().set_aspect('equal')  # Ensure the orbits are not distorted
plt.legend()
plt.title("Gliese 876 System Orbits")
plt.xlabel("x [light-seconds]")
plt.ylabel("y [light-seconds]")
plt.grid(True)
plt.show()
