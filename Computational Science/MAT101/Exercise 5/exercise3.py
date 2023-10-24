from time import perf_counter_ns as timer

def while_sum(n):
    if not isinstance(n, (int, float)) or n <= 0:
        return ValueError("n must be an integer or float and larger than zero")
    
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def for_sum(n):
    if not isinstance(n, (int, float)) or n <= 0:
        return ValueError("n must be an integer or float and larger than zero")
    
    total = 0
    for i in range(1, n+1):
        total += i
        
    return total

def gauss_summation(n):
    if not isinstance(n, (int, float)) or n <= 0:
        return ValueError("n must be an integer or float and larger than zero")
    
    return n*(n+1)/2

if __name__ == "__main__":
    start_time_while = timer()
    result_while = while_sum(10000)
    end_time_while = timer()
    
    start_time_for = timer()
    result_for = for_sum(10000)
    end_time_for = timer()
    
    start_time_gauss = timer()
    result_gauss = gauss_summation(10000)
    end_time_gauss = timer()
    
    start_built_in = timer()
    result_built_in = sum(range(1, 10001))
    end_built_in = timer()
    
    elapsed_time_while = end_time_while - start_time_while
    elapsed_time_for = end_time_for - start_time_for
    elapsed_time_gauss = end_time_gauss - start_time_gauss
    elapsed_built_in = end_built_in - start_built_in
    
    print(f"Result While: {result_while}, Elapsed time: {elapsed_time_while} ns")
    print(f"Result For: {result_for}, Elapsed time: {elapsed_time_for} ns")
    print(f"Result Gauss: {result_gauss}, Elapsed time: {elapsed_time_gauss} ns")
    print(f"Result Built-in: {result_built_in}, Elapsed time: {elapsed_built_in} ns")
    
    """
    e)
    Result While: 50005000, Elapsed time: 1'714'230 ns
    Result For: 50005000, Elapsed time: 1'013'028 ns
    Result Gauss: 50005000.0, Elapsed time: 28'273 ns
    Result Built-in: 50005000, Elapsed time: 394'715 ns
    
    I would generally just use the built-in sum function, but if I had to choose between the three, I would use the Gauss summation formula.
    """