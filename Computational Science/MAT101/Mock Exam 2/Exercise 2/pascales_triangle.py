from math import factorial

def pascals_triangle(n):
    if n <= 0:
        print("n must be a non-negative integer larger than 0.")
    
    for i in range(n):
        print(" " * (n - i), end="")
        for j in range(i + 1):
            print((factorial(i) // (factorial(j) * factorial(i - j))) % 2, end=" ")
        print()

def mandelbrot(c, n, curr = 0):
    if n == 0:
        return curr
    else:
        return mandelbrot(c, n - 1, curr ** 2 + c)
    
def generate_sequence(c, num_elements=10):

    sequence = [mandelbrot(c, n) for n in range(num_elements)]

    return sequence



if __name__ == "__main__":
    c_1_outputs = generate_sequence(1)
    c_negative_1_outputs = generate_sequence(-1)
    
    print("c = 1:", c_1_outputs)
    # The values quickly escalate to extremely large numbers. This indicates that the sequence does not remain bounded, and therefore c=1c=1 does not belong to the Mandelbrot set.
    
    print("c = -1:", c_negative_1_outputs)
    #The sequence alternates between 0 and −1, which means it remains bounded. Therefore, c=−1 does belong to the Mandelbrot set because the sequence does not tend towards infinity.
