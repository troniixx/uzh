import matplotlib.pyplot as plt
import math

def partial_sum(x):
    sol = 0

    for i in range(x+1):
        sol += (-1)**i * (1/(2*i+1))
    
    return sol

def convergence_vector(l):
    output = []
    
    for element in l:
        output.append(partial_sum(element))

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
    pass


if __name__ == '__main__':
    p = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    plotter(p)