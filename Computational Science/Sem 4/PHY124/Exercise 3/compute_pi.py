from decimal import Decimal, getcontext

def arctan(x, precision=1000):
    getcontext().prec = precision + 5  #precision slightly higher to reduce rounding errors
    x = Decimal(x)
    term = x  # T0 = x
    sum_arctan = x  # Initialize the sum
    n = 1

    while term != 0:
        term *= -x**2  #next term Tk = -x^2 * Tk-1
        sum_arctan += term / (2 * n + 1)  # divided by (2k + 1)
        n += 1

    return sum_arctan

def compute_pi(precision=1000):
    getcontext().prec = precision + 5
    arctan_half = arctan(Decimal(1) / 2, precision)
    arctan_third = arctan(Decimal(1) / 3, precision)
    
    pi = 4 * (arctan_half + arctan_third)

    return +pi.quantize(Decimal(10) ** -precision)  # Round to requested number of decimal places

# Compute π to 1000 decimal places
pi_1000_digits = compute_pi(1000)
print(pi_1000_digits[901:913])
