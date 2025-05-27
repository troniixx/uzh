import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Simulation Parameters ---
Nx = 200                      # Number of spatial grid points
x = np.linspace(-5, 5, Nx)    # 1D spatial domain from -5 to 5
dx = x[1] - x[0]              # Spatial step size
dt = 0.0002                   # Time step size (controls numerical stability)
Nt = 500                      # Total number of animation frames

# --- Potential Energy Function (Harmonic Oscillator) ---
V = 0.5 * x**2                # V(x) = 1/2 * x^2 for a quantum harmonic oscillator

# --- Initial Wavefunction: Superposition of Ground and First Excited State ---
# Real part
psi_real = np.exp(-x**2 / 2) + x * np.exp(-x**2 / 2)
psi_imag = np.zeros_like(x)  # Imaginary part initially zero

# --- Normalize the Wavefunction ---
# Compute norm: ∫|ψ|² dx ≈ Σ|ψ|² * dx
norm = np.sqrt(np.sum((psi_real**2 + psi_imag**2) * dx))
psi_real /= norm
psi_imag /= norm

# --- Finite Difference Laplacian Matrix (2nd derivative) ---
laplacian = np.zeros((Nx, Nx))  # Initialize Laplacian matrix
for i in range(1, Nx - 1):
    laplacian[i, i - 1] = 1     # Off-diagonal left
    laplacian[i, i] = -2        # Diagonal center
    laplacian[i, i + 1] = 1     # Off-diagonal right
laplacian /= dx**2              # Scale by 1/dx^2

# --- Set Up Plot for Animation ---
fig, ax = plt.subplots()
line, = ax.plot(x, psi_real**2 + psi_imag**2)  # Initial probability density
ax.set_ylim(0, 1.2 * np.max(psi_real**2 + psi_imag**2))  # Set y-axis range
ax.set_title(r"Leapfrog: $|\psi(x,t)|^2$")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")

# --- Leapfrog Time Evolution Function ---
# This will be called once per animation frame
def update(frame):
    global psi_real, psi_imag

    steps_per_frame = 10  # Do multiple simulation steps per frame for faster animation

    for _ in range(steps_per_frame):
        # Compute Laplacian of real part
        psi_r_lap = laplacian @ psi_real
        # Update imaginary part using Schrödinger equation
        psi_imag += dt * (0.5 * psi_r_lap - V * psi_real)

        # Compute Laplacian of imaginary part
        psi_i_lap = laplacian @ psi_imag
        # Update real part
        psi_real -= dt * (0.5 * psi_i_lap - V * psi_imag)

    # Update the plot with new probability density
    probability_density = psi_real**2 + psi_imag**2
    line.set_ydata(probability_density)
    return line,

ani = animation.FuncAnimation(fig, update, frames=Nt, interval=1, blit=False)
plt.show()
