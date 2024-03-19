import math
import numpy as np
import matplotlib.pyplot as plt

def my_sequence(N: int, t: int, s: str):
    li = []
    lv = []
    
    if s == "geq":
        for i in range(N+1):
            if math.sin((2*np.pi*i) / 100) >= t:
                li.append(i)
                lv.append(math.sin((2*np.pi*i) / 100))
                
    elif s == "leq":
        for i in range(N+1):
            if math.sin((2*np.pi*i) / 100) <= t:
                li.append(i)
                lv.append(math.sin((2*np.pi*i) / 100))

    else:
        return ValueError("Invalid string")
    
    return li, lv
    
def plotter(N, t, s):
    indices, values = my_sequence(N, t, s)
    plt.plot(indices, values, 'o')
    plt.grid(True)
    plt.xlabel("k")
    plt.ylabel("a(k)")
    plt.title(s)
    plt.savefig("plot_" + s + ".pdf")
    plt.show()

if __name__ == "__main__":
    plotter(1000, 0, "geq")
    plotter(1000, 0, "leq")