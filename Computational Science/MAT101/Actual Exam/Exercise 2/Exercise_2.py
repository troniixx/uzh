def divisors(n):
    # check if the number is greater than 0
    if n <= 0:
        return "The number must be greater than 0"
    
    # iterate through the numbers from 1 to n
    divisors = []
    for i in range(1, n+1):
        # and check if the number is a divisor by using modulo operator
        if n % i == 0:
            divisors.append(i)
            
    return divisors

def GCD(a, b):
    #everthing is a divisor of 0
    if (a == 0):
        return b
    if (b == 0):
        return a
    # base case
    if (a == b):
        return a
    # a is greater
    if (a > b):
        return GCD(a-b, b)
    return GCD(a, b-a)
    
class Fraction():
    # initialize the class with the numerator and the denominator
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # print the fraction
    def print(self):
        print(f"{self.numerator}/{self.denominator}")
    
    # return the inverse of the fraction by swapping the numerator and the denominator from init
    def inverse(self):
        return Fraction(self.denominator, self.numerator)
    
    # reduce the fraction by dividing the numerator and the denominator by their greatest common divisor
    def reduce(self):
        gcd = GCD(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)
    
    # add two fractions by overriding the __add__ method
    def __add__(self, other):
        if not isinstance(self, Fraction) or not isinstance(other, Fraction):
            return "Both must be objects of the class Fraction!"
        
        # using the formula for adding fractions and then returning a new Fraction object with
        # the new numerator and the new denominator
        # a/b + c/d = (a*d + b*c) / (b*d)
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        
        return Fraction(new_numerator, new_denominator)
    
    
if __name__ == "__main__":
    # testing the Fraction class
    one = Fraction(1, 2)
    two = Fraction(2, 3)
    three = Fraction(10, 20)
    
    (one+two).print() # should return 7/6 --> OK: print() and + works
    (one.inverse()).print() # should return 2/1 --> OK: inverse() works
    (three.reduce()).print() # should return 1/2 --> OK: reduce() works
    
    # testing the divisors and GCD functions
    print(divisors(10)) # should return [1, 2, 5, 10] --> OK
    print(divisors(0)) # should return "The number must be greater than 0" --> OK
    print(GCD(100, 60)) # should return 20 --> OK
    print(GCD(0, 0)) # should return 0 --> OK
    print(GCD(0, 10)) # should return 10 --> OK
    print(GCD(10, 0)) # should return 10 --> OK
    print(GCD(278, 147)) # should return 1 --> OK