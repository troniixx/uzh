import numpy as np

def monteCarloPi(N: int) -> float:
    points = 0
    for _ in range(N):
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points += 1
            
    return 4*(points/N)

def monteCarloSphere(N: int, d: int) -> float:
    points = 0
    for _ in range(N):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        z = np.random.uniform(-1, 1)
        if x**2 + y**2 + z**2 <= 1:
            points += 1
    
    return (2**d)*(points/N)

if __name__ == "__main__":
    #print(monteCarloPi(1000000))
    print(monteCarloSphere(10000, 100))
    