import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
Nx = 200                      # number of spatial grid points
x = np.linspace(-5, 5, Nx)    # spatial domain
dx = x[1] - x[0]              # spatial step
dt = 0.0002                   # time step
Nt = 500                      # number of time steps

# Potential: Harmonic oscillator
V = 0.5 * x**2

# Initial wavefunction: superposition of ground and first excited state
psi_real = np.exp(-x**2 / 2) + x * np.exp(-x**2 / 2)
psi_imag = np.zeros_like(x)

# Normalize the wavefunction
norm = np.sqrt(np.sum((psi_real**2 + psi_imag**2) * dx))
psi_real /= norm
psi_imag /= norm

# Laplacian operator using finite differences (Dirichlet)
laplacian = np.zeros((Nx, Nx))
for i in range(1, Nx - 1):
    laplacian[i, i - 1] = 1
    laplacian[i, i] = -2
    laplacian[i, i + 1] = 1
laplacian /= dx**2

# Precompute plot
fig, ax = plt.subplots()
line, = ax.plot(x, psi_real**2 + psi_imag**2)
ax.set_ylim(0, 1.2 * np.max(psi_real**2 + psi_imag**2))
ax.set_title(r"Leapfrog: $|\psi(x,t)|^2$")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")

# Leapfrog step: update psi_real and psi_imag alternately
def update(frame):
    global psi_real, psi_imag
    steps_per_frame = 5  # do 5 leapfrog steps per animation frame
    for _ in range(steps_per_frame):
        psi_r_lap = laplacian @ psi_real
        psi_imag += dt * (0.5 * psi_r_lap - V * psi_real)

        psi_i_lap = laplacian @ psi_imag
        psi_real -= dt * (0.5 * psi_i_lap - V * psi_imag)

    probability_density = psi_real**2 + psi_imag**2
    line.set_ydata(probability_density)
    return line,


# Animate
ani = animation.FuncAnimation(fig, update, frames=Nt, interval=10)
plt.show()
