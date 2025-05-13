import numpy as np
def simple_circuit():
    M = np.array([[2, -1, -1, 0],
                [-1, 3, -1, -1],
                [-1, -1, 3, -1],
                [0, -1, -1, 2]])

    b = np.array([1, 0, 0, -1])
    x = np.linalg.solve(M, b)

    print("Simple Circuit")
    for i in range(len(x)):
        print(f"x{i+1} = {x[i]:.2f}")


if __name__ == "__main__":
    simple_circuit()
