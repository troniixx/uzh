def leapfrog_integration():
    g = 9.81
    dt = 0.001
    total_time = 3.9

    x = 0.0
    y = 0.0
    vx = 14.0
    vy = 11.0

    n_steps = int(total_time / dt)

    vx_half = vx + 0 * dt/2
    vy_half = vy - g * dt/2
    
    # Main integration loop
    for _ in range(n_steps):

        x += vx_half * dt
        y += vy_half * dt

        vy_half -= g * dt

    return x, y

if __name__ == "__main__":
    x_final, y_final = leapfrog_integration()
    print(f"Position at t=3.9s: x = {x_final:.4f} m, y = {y_final:.4f} m")

"""
https://lemesurierb.people.charleston.edu/numerical-methods-and-analysis-python/main/ODE-IVP-6-multi-step-methods-introduction-python.html
"""