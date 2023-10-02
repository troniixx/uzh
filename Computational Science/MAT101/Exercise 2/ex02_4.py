from math import gcd

def eulers_totient(n):
    euler_phi = 0
    for int in range(1, n):
        if gcd(n, int) == 1:
            euler_phi += 1
    
    return euler_phi

if __name__ == "__main__":
    print(eulers_totient(10))
    print(eulers_totient(11))
    print(eulers_totient(13))
    print(eulers_totient(69))
    print(eulers_totient(420))
    