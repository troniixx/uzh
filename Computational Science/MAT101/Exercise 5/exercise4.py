def my_primefactors(n):
    if not isinstance(n, int) or n <= 0:
        return ValueError("n must be an integer and larger than zero")
    
    primes = [2, 3, 5, 7]
    sol_list = []
    while n >= 1:
        for prime in primes:
            if n % prime == 0:
                n = n / prime
                sol_list.append(prime)
                
    return sol_list

if __name__ == '__main__':
    print(my_primefactors(10))