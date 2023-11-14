import numpy as np

def monteCarloPi(N: int) -> float:
    points = 0
    for _ in range(N):
        x, y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points += 1
            
    return 4*(points/N)

def monteCarloSphere(N: int, d: int) -> float:
    points = np.random.uniform(-1, 1, (N, d))
    distances = np.sum(points**2, axis=1)
    points_sphere = np.sum(distances <= 1)
    volume = 2**d
    
    return (points_sphere / N) * volume

if __name__ == "__main__":
    #print(monteCarloPi(1000000))
    print(monteCarloSphere(1000000, 10))

"""
the non spheric way of doing it approximates pi, while the spheric way approximates the volume of a sphere and will only come close
to pi if the dimension is low enough and N is high enough (close to infinity)
"""