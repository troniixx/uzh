import numpy as np
import matplotlib.pyplot as plt

def leapfrog(f_acceleration, y0, v0, dt, n_steps):
    y = np.zeros(n_steps)
    y[0] = y0
    v_half = v0 + 0.5 * dt * f_acceleration(y0, 0)

    for i in range(1, n_steps):
        y[i] = y[i-1] + dt * v_half
        v_half += dt * f_acceleration(y[i], i * dt)

    return y

def pendulum_acc(phi, tau):
    gamma = 0.25
    lambda_ = 0.075
    return -gamma * np.sin(phi) - lambda_ * np.sin(phi - tau)

def plotter(y, dt):
    t = np.arange(len(y)) * dt
    plt.plot(t, y)
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.title('Pendulum Angle vs Time')
    plt.grid()
    plt.show()

y = leapfrog(pendulum_acc, y0=0.1, v0=0.0, dt=0.01, n_steps=5000)
print(y)
plotter(y, dt=0.01)

"""
https://lemesurierb.people.charleston.edu/numerical-methods-and-analysis-python/main/ODE-IVP-6-multi-step-methods-introduction-python.html
https://en.wikipedia.org/wiki/Leapfrog_integration
"""