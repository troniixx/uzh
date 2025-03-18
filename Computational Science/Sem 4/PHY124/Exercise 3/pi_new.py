from fractions import Fraction

def calculate_arctan(x, precision):
    # Convert x to a Fraction if it's not already
    x = Fraction(x)
    x_squared = x * x
    
    # Initialize the first term and the sum
    term = x  # T_0 = x
    result = Fraction(0)
    
    # Calculate the sum
    for k in range(precision):
        result += term / (2 * k + 1)
        # Calculate the next term
        term = -x_squared * term
    
    return result

def calculate_pi(precision):
    arctan_half = calculate_arctan(Fraction(1, 2), precision)
    arctan_third = calculate_arctan(Fraction(1, 3), precision)
    
    pi = 4 * (arctan_half + arctan_third)
    
    return pi

def fraction_to_string(fraction, decimal_places=1000):
    # Get integer part and remainder
    integer_part = fraction.numerator // fraction.denominator
    remainder = fraction.numerator % fraction.denominator
    
    # Start with integer part
    result = str(integer_part) + "."
    
    # Calculate decimal digits
    for _ in range(decimal_places):
        remainder *= 10
        digit = remainder // fraction.denominator
        result += str(digit)
        remainder %= fraction.denominator
    
    return result

if __name__ == "__main__":
    precision = 2000
    pi_fraction = calculate_pi(precision)
    pi_string = fraction_to_string(pi_fraction, 1000)
    
    print(pi_string)
    print(pi_string[901:913])