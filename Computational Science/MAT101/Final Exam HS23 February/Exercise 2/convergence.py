import matplotlib.pyplot as plt
import math

def partial_sum(x):
    sol = 0

    for i in range(x+1):
        sol += (-1)**i * (1/(2*i+1))
    
    return sol

def convergence_vector(v):
    max_index = max(v)
    partial_sum = 0
    output = []

    for i in range(max_index + 1):
        partial_sum += (-1)**i / (2*i + 1)
        if i in v:
            output.append(partial_sum)

    return output

def plotter(l):
    p = convergence_vector(l)
    
    pilist = [math.pi/4] * len(l)

    plt.xscale("log")
    plt.plot(l, p, "o", color = "green", label = "partial sums")
    plt.axhline(y=math.pi/4, color='red', linestyle='-', label='π/4')
    plt.title("Exercise 2 plots")
    plt.xlabel("log scale")
    plt.ylabel("Convergence")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig("Computational Science/MAT101/Final Exam HS23 February/Exercise 2/plot_convergence.pdf")

def convergence_up_to_tolerance(t, m):
    prev = 0

    for n in range(1, m+1):
        curr = prev + (-1)**(n-1) / ((2*n - 1) + 1)

        if abs(curr - prev) <= t:
            return n
        
        prev = curr
    
    return "Condition not met for n <= m"


if __name__ == '__main__':
    p = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    #convergence_vector(p)

    #plotter(p)

    epsilon = 0.01
    m = 1000
    print(convergence_up_to_tolerance(epsilon, m))