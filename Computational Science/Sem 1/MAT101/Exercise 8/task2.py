import matplotlib.pyplot as plt
import numpy as np

def plot_subplots(x_min, x_max):
    fig, axs = plt.subplots(2, 2)
    fig.suptitle("exp(e)")

    x_values = np.linspace(x_min, x_max, 100)
    y = np.exp(x_values)

    axs[0, 0].plot(x_values, y, color="green")
    axs[0, 0].set_xlabel("x")
    axs[0, 0].set_ylabel("exp(x)")

    axs[0, 1].plot(x_values, y, color="blue")
    axs[0, 1].set_xlabel("x")
    axs[0, 1].set_ylabel("exp(x)")
    axs[0, 1].set_xscale('log')

    axs[1, 0].plot(x_values, y, color="red")
    axs[1, 0].set_xlabel("x")
    axs[1, 0].set_ylabel("exp(x)")
    axs[1, 0].set_yscale('log')

    axs[1, 1].plot(x_values, y, color="purple")
    axs[1, 1].set_xlabel("x")
    axs[1, 1].set_ylabel("exp(x)")
    axs[1, 1].set_xscale('log')
    axs[1, 1].set_yscale('log')

    plt.tight_layout()
    plt.show()


def plot_subplots_b(x_min, x_max, grid=False, function=np.exp):
    fig, axs = plt.subplots(2, 2)
    fig.suptitle(f"{str(function)}")

    x_values = np.linspace(x_min, x_max, 100)
    y = function(x_values)

    axs[0, 0].plot(x_values, y, color="green")
    axs[0, 0].set_xlabel("x")
    axs[0, 0].set_ylabel("y")
    axs[0, 0].grid(grid)

    axs[0, 1].plot(x_values, y, color="red")
    axs[0, 1].set_xlabel("x")
    axs[0, 1].set_ylabel("y")
    axs[0, 1].set_xscale("log")
    axs[0, 1].grid(grid)

    axs[1, 0].plot(x_values, y, color="blue")
    axs[1, 0].set_xlabel("x")
    axs[1, 0].set_ylabel("y")
    axs[1, 0].set_yscale("log")
    axs[1, 0].grid(grid)

    axs[1, 1].plot(x_values, y, color="purple")
    axs[1, 1].set_xlabel("x")
    axs[1, 1].set_ylabel("y")
    axs[1, 1].set_xscale("log")
    axs[1, 1].set_yscale("log")
    axs[1, 1].grid(grid)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    #plot_subplots(1, 100)
    plot_subplots_b(0.1, 10, True, np.cos)