def gcd(a, b):
    if (b == 0):
        greatest_common_divisor = a
        return greatest_common_divisor
    else:
        greatest_common_divisor = gcd(b, a % b)
        return greatest_common_divisor
    
def lcm(a, b):
    if a == 0 or b == 0:
        least_common_multiple = 0
        return least_common_multiple
    else:
        least_common_multiple = abs(a * b) / gcd(a, b)
    
    return least_common_multiple
    
if __name__ == "__main__":
    print("GCD")
    print(gcd(12, 8))
    print(gcd(8, 12))
    print(gcd(12, 12))
    print(gcd(12, 0))
    print(gcd(0, 12))
    print(gcd(0, 0))
    
    print("\nLCM")
    print(lcm(12, 8))
    print(lcm(8, 12))
    print(lcm(12, 8))
    print(lcm(12, 0))
    print(lcm(0, 12))
    print(lcm(0, 0))
    