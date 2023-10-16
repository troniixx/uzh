#Exercise 1a and 1b
def power(base, exponent):
    if not isinstance(base, (int, float)):
        return TypeError("Base must be a number")
    """
    I prefer doing error handling like this because it looks much cleaner :).
    To show that I know how to do it as specified:

        if not isinstance(base, (int, float)):
            print("Base must be a number")
            return None
    """
    if not isinstance(exponent, int):
        return TypeError("Exponent must be an integer")   
    if exponent < 0:
        return TypeError("Exponent must be a positive integer")
        
    else:
        result = 1
        for i in range(exponent):
            result = result * base
        return result

#Exercise 1c and 1d
def better_power(base, exponent):
    if not isinstance(base, (int, float)):
        return TypeError("Base must be a number")
    if not isinstance(exponent, int):
        return TypeError("Exponent must be an integer")   
    if base == 0 and exponent < 0:
        return TypeError("Base must be a non-zero number and exponent must be a positive integer")
    if exponent < 0:
        return TypeError("Exponent must be a positive integer")
        
    else:
        result = 1
        for i in range(exponent):
            result = result * base
        return result
    
    
if __name__ == '__main__':
    print("Power: \n")
    print(power(2, 3))
    print(power(2, 0))
    print(power(2.5, 2))
    print(power(2, -1))
    print(power(2.5, -1))
    print(power('a', 2))
    print(power(2, 'a'))
    print(power(2.5, 'a'))
    print(power('a', 'a'))
    
    print("\nBetter Power: \n")
    print(better_power(0, -1))
    print(better_power(2, 3))
    print(better_power(2, 0))
    print(better_power(2.5, 2))
    print(better_power(2, -1))
    print(better_power(2.5, -1))
    print(better_power('a', 2))
    print(better_power(2, 'a'))
    print(better_power(2.5, 'a'))
    print(better_power('a', 'a'))

    
