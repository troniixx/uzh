import matplotlib.pyplot as plt

def reader(path):
    i = []
    x_i = []
    y_i = []

    with open(path, "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            i.append(int(line.split(", ")[0]))
            x_i.append(float(line.split(", ")[1]))
            y_i.append(float(line.split(", ")[2]))

    return i, x_i, y_i

def plotter(path):
    i, x_i, y_i = reader(path)

    plt.plot(i, x_i, color = "blue", label = "x_i", linestyle = "dotted")
    plt.plot(i, y_i, color = "red", label = "y_i", linestyle = "dashed")
    plt.title("Exercise 3 plots")
    plt.xlabel("i")
    plt.ylabel("x_i, y_i")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig("Computational Science/MAT101/Final Exam HS23 February/Exercise 3/my_plot.pdf")

def write(read, write):
    i, x_i, y_i = reader(read)

    with open(write, "w") as f:
        f.write("i, y_i, x_i\n")
        for j in range(len(i)):
            f.write(f"{i[j]}, {y_i[j]}, {x_i[j]}\n")


if __name__ == "__main__":
    path = "Computational Science/MAT101/Final Exam HS23 February/Exercise 3/my_function.dat"
    plotter(path)

    writer = "Computational Science/MAT101/Final Exam HS23 February/Exercise 3/my_switch.dat"
    write(path, writer)