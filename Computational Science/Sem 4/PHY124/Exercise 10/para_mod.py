import numpy as np
from scipy.integrate import odeint

def ode(state, t, g=9.81):
    x, y, vx, vy = state
    return [vx, vy, 0, -g]

def leapfrog_integration_odeint():
    g = 9.81
    total_time = 4.7
    dt = 0.001
    t = np.arange(0, total_time + dt, dt)

    initial_state = [0.0, 0.0, 8.0, 14.0]
    solution = odeint(ode, initial_state, t, args=(g,))

    x_final, y_final = solution[-1, 0], solution[-1, 1]
    return x_final, y_final

if __name__ == "__main__":
    x_final, y_final = leapfrog_integration_odeint()
    print(f"x = {x_final:.4f} m, y = {y_final:.4f} m")
    print(f"{x_final},{y_final}")