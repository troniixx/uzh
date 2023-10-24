def my_primefactors(n):
    if not isinstance(n, int) or n <= 0:
        return ValueError("n must be an integer and larger than zero")
    
    primes = []
    
    