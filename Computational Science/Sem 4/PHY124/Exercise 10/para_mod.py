from scipy.integrate import odeint
import numpy as np

def projectile_motion(state, t):
    x, y, vx, vy = state
    g = 9.81
    dxdt = vx
    dydt = vy
    dvxdt = 0.0
    dvydt = -g
    return [dxdt, dydt, dvxdt, dvydt]

def solve_projectile_odeint():
    x0 = 0.0
    y0 = 0.0
    vx0 = 14.0
    vy0 = 11.0
    initial_state = [x0, y0, vx0, vy0]

    total_time = 4.7
    t = np.linspace(0, total_time, 1000)

    sol = odeint(projectile_motion, initial_state, t)

    return t, sol

if __name__ == "__main__":
    t, y = solve_projectile_odeint()
    x_final = y[-1, 0]
    y_final = y[-1, 1]
    print(f"Position at t=4.7s: x = {x_final:.4f} m, y = {y_final:.4f} m")
