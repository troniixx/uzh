from cmath import sqrt as sq

def quadratic_formula(a, b, c):
    """
    (-b +- sqrt(b^2 - 4ac))/(2a)
    """
    if not isinstance(a, (int, float, complex)) or not isinstance(b, (int, float, complex)) or not isinstance(c, (int, float, complex)):
        return ValueError("input must be a either float, int or complex")
    if a == 0:
        return ValueError("a must not be zero")
    
    discriminant = b**2 - 4*a*c #(b^2 - 4ac)
    
    x_n = (-b + sq(discriminant))/(2*a)
    x_p = (-b - sq(discriminant))/(2*a)
    
    return [x_n, x_p]

if __name__ == '__main__':
    print(quadratic_formula(1,0,1))
    print(quadratic_formula(0,1,1))
    print(quadratic_formula(1.0,0,0))
    print(quadratic_formula(1j,0,2))
    print(quadratic_formula(1,1,1))
    print(quadratic_formula(-1,-1,-1))
    print(quadratic_formula("a",0,-1))
    print(quadratic_formula(-1,0,-1))
    