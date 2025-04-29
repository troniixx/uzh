import numpy as np
import matplotlib.pyplot as plt

df = np.loadtxt("/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 4/PHY124/Exercise 10/gliese876ini.txt")

M = df[:, 0]
X = df[:, 1]
Y = df[:, 2]
V_x = df[:, 3]
V_y = df[:, 4]

positions = np.stack((X, Y), axis=1)
velocities = np.stack((V_x, V_y), axis=1)

def leapfrog(masses, positions, velocities, dt, n_steps):
    N = len(masses)
    traj = np.zeros((n_steps, N, 2))  # Store all positions
    traj[0] = positions.copy()

    # Initial acceleration
    acc = compute_accelerations(positions, masses)

    # Half-step velocity
    velocities += 0.5 * dt * acc

    for step in range(1, n_steps):
        # Full-step position update
        positions += dt * velocities

        # Compute new accelerations
        acc = compute_accelerations(positions, masses)

        # Full-step velocity update
        velocities += dt * acc

        # Save position
        traj[step] = positions.copy()

    return traj

def compute_accelerations(positions, masses):
    N = len(masses)
    accelerations = np.zeros_like(positions)
    for i in range(N):
        for j in range(N):
            if i != j:
                r = positions[j] - positions[i]
                dist = np.linalg.norm(r)
                accelerations[i] += masses[j] * r / dist**3
    return accelerations

# Simulation parameters
dt = 1000  # seconds, must be < 3600
n_steps = 20000  # tune as needed

trajectory = leapfrog(M, positions, velocities, dt, n_steps)

plt.figure(figsize=(8, 8))
for i in range(len(M)):
    plt.plot(trajectory[:, i, 0], trajectory[:, i, 1], label=f"Body {i}")
plt.gca().set_aspect('equal')
plt.legend()
plt.title("Gliese 876 System Orbits")
plt.xlabel("x [light-seconds]")
plt.ylabel("y [light-seconds]")
plt.grid(True)
plt.show()
