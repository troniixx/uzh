import math
import matplotlib.pyplot as plt


# ****--- START Reading data from input_data.dat ---****

with open("Computational Science/MAT101/Rep Exam 22/Exercise 2/input_data.dat", "r") as file:
    data = file.read().splitlines()
    
x_n = []
y_n = []

for line in data[1:]:
    x, y = line.split(", ")
    x_n.append(float(x))
    y_n.append(float(y))
    
# ****--- END Reading data from input_data.dat ---****
    

# ****--- START Plotting ---****

cos_values = [math.cos(2 * math.pi * x) for x in x_n]

plt.plot(x_n, y_n, "o", color = "blue", label =  "Input", linestyle = "solid")
#plot cos(2*pi*x)
plt.plot(x_n, cos_values, "o", color = "red", label = "cos(2*pi*x)", linestyle = "dashed")
plt.title("Data from input_data.dat and cos(2*pi*x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("Computational Science/MAT101/Rep Exam 22/Exercise 2/my_plot.pdf")
plt.show()

# ****--- END Plotting ---****

# ****--- START Getting Error values ---****

err = []
for i in range(1001):
    err.append(abs(y_n[i] - cos_values[i]))
    
with open("Computational Science/MAT101/Rep Exam 22/Exercise 2/my_error.dat", "w") as file:
    file.write("x, y, cos(2*pi*x), error\n")
    for i in range(1001):
        file.write(f"{x_n[i]}, {y_n[i]}, {cos_values[i]}, {err[i]}\n")

# ****--- END Getting Error values ---****