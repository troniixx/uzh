def fibonacci_recursive(n: int) -> int:
    if not isinstance(n, int) or n < 0: return -1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
    
def fibonacci_iterative(n: int) -> int:
    if not isinstance(n, int) or n < 0: return -1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
    
if __name__ == '__main__':
    print("Recursive: ")
    print(fibonacci_recursive(-1))
    print(fibonacci_recursive("a"))
    print(fibonacci_recursive(1))
    print(fibonacci_recursive(0))
    print(fibonacci_recursive(19))
    print(fibonacci_recursive(38)) #b) the larger the number the longer it takes to compute
    
    print("\nIterative: ")
    print(fibonacci_iterative(-1))
    print(fibonacci_iterative("a"))
    print(fibonacci_iterative(1))
    print(fibonacci_iterative(0))
    print(fibonacci_iterative(19))
    print(fibonacci_iterative(38))