def my_primefactors(n):
    if not isinstance(n, int) or n <= 0:
        return ValueError("n must be an integer and larger than zero")
    
    sol_list = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            n = n / divisor
            sol_list.append(divisor)
        divisor += 1
                
    return sol_list

if __name__ == '__main__':
    print(my_primefactors(10))