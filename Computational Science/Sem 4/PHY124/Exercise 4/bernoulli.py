from fractions import Fraction

def factorial_list(n):
    fact = [1]
    for i in range(1, n + 1):
        fact.append(fact[i - 1] * i)
    return fact

def bernoulli_numbers(n):
    fact_list = factorial_list(n + 1)
    B = [Fraction(1)]

    for m in range(1, n + 1):
        sum_term = 0
        for k in range(m):
            sum_term += (fact_list[m] * B[k]) / (fact_list[k] * fact_list[m - k + 1])
        B.append(-sum_term)


    return B

n = 50
B_numbers = bernoulli_numbers(n)
print(B_numbers[-1])
