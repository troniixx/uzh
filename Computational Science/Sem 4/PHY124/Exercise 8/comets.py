from rootfinder import root
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------#

def halley_f(psi, t, e):
    return psi - e * np.sin(psi) - t

def halley_f_prime(psi, e):
    return 1 - e * np.cos(psi)

e_halley = 0.967
a_halley = 17.8
t_vals_halley = np.linspace(0, 2*np.pi, 500)
x_halley, y_halley = [], []

for t in t_vals_halley:
    # these functions help to pass through
    def f(psi):
        return halley_f(psi, t, e_halley)
    def f_prime(psi):
        return halley_f_prime(psi, e_halley)
    
    try:
        psi = root(f, f_prime, x_0 = t)
        x = a_halley * (np.cos(psi) - e_halley)
        y = a_halley * np.sqrt(1 - e_halley**2) * np.sin(psi)
        x_halley.append(x)
        y_halley.append(y)
    except ValueError as e:
        print(f"Error for t={t}: {e}")
        continue
    
# ------------------------------------------------------------------------------------#

def oumuamua_f(psi, t, e):
    return e * np.sinh(psi) - psi - t

def oumuamua_f_prime(psi, e):
    return e * np.cosh(psi) - 1

e_oumuamua = 1.20
a_oumuamua = 1.28
#t_vals_oumuamua = np.linspace(-np.pi, np.pi, 2000)
t_vals_oumuamua = np.linspace(-20, 20, 2000)
x_oumuamua, y_oumuamua = [], []

for t in t_vals_oumuamua:
    # these functions 
    def f(psi):
        return oumuamua_f(psi, t, e_oumuamua)
    def f_prime(psi):
        return oumuamua_f_prime(psi, e_oumuamua)
    
    try:
        psi = root(f, f_prime, x_0 = t)
        x = a_oumuamua * (e_oumuamua - np.cosh(psi))
        y = a_oumuamua * np.sqrt(e_oumuamua**2 - 1) * np.sinh(psi)
        x_oumuamua.append(x)
        y_oumuamua.append(y)
    except ValueError as e:
        print(f"Error for t={t}: {e}")
        continue
# ------------------------------------------------------------------------------------#

plt.figure(figsize=(8, 8))
plt.plot(x_halley, y_halley, label="Halley's Comet")
plt.plot(x_oumuamua, y_oumuamua, label="Oumuamua", linestyle="--")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()