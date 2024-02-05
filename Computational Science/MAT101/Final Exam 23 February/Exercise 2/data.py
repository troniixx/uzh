import matplotlib.pyplot as plt

def reader(path):
    with open(path, "r") as f:
        t_n = []
        f_n = []

        lines = f.readlines()[1:]
        for line in lines:
            t, f = line.split(", ")
            t_n.append(float(t))
            f_n.append(float(f))

    return t_n, f_n

def plotter(path):
    t, f = reader(path)

    plt.plot(t, f, label = "f(t)", color = "red")
    plt.axhline(y = 5, color = "green", linestyle = "--", label = "5")
    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig("Computational Science/MAT101/Final Exam 23 February/Exercise 2/my_plot.pdf")
        
def writer(r, w):
    t, f = reader(r)

    min_t = min(t)
    max_t = max(t)
    min_f = min(f)
    max_f = max(f)

    with open(w, "w") as f:
        f.write(f"{min_f};{max_f}")

if __name__ == "__main__":
    r = "Computational Science/MAT101/Final Exam 23 February/Exercise 2/time_evolution.dat"
    w = "Computational Science/MAT101/Final Exam 23 February/Exercise 2/my_min_max.dat"

    plotter(r)
    writer(r, w)