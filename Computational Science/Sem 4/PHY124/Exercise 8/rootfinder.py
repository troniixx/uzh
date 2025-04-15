"""
f(x) = x^3 + x - 96
f(x) = 0
f' = 3x^2 + 1

x_new = x_old - f(x_old)/f'(x_old)
"""
def f(x):
    return x**3 + x - 96

def f_prime(x):
    return 3*x**2 + 1

def root(f, f_prime, x_0=1.0):
    x = x_0
    tol = 1e-15 # approximatly the precision limit of a float
    max_iter = 100000
    
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        
        if fpx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        
        x_new = x - fx / fpx
        
        # check if converged
        if abs(x_new - x) < tol:
            return round(x_new, 10)
        
        x = x_new
        
    raise ValueError("Maximum iterations reached. No solution found.")

if __name__ == "__main__":
    sol = root(f, f_prime)
    print(sol)

