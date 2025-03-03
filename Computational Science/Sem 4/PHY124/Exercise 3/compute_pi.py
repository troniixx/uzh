def arctan(x, terms=5000):
    term = x
    arctan_sum = term
    
    for k in range(1, terms):
        term *= -x**2
        arctan_sum += term / (2*k + 1)
    
    return arctan_sum


sol = str(4*(arctan(1/2, 15000) + arctan(1/3, 15000)))
print(sol)