def f(num):
    if not isinstance(num, int) or num < 0:
        raise TypeError("num must be a positive integer")
    else:
        if num % 2 == 0:
            return num // 2
        else:
            return 3 * num + 1

def collatz(num):
    if not isinstance(num, int) or num < 0:
        raise TypeError("num must be a positive integer")
    
    result = []
    
    while num != 1:
        result.append(num)
        num = f(num)

    result.append(1)
    return result

#NOTE Bonus Exercise
# Its only 5 lines but i never thought that it would take such a long time to come up with it
def longest_collatz():
    longest = []
    for num in range(1, 10001):
        if len(collatz(num)) > len(longest):
            longest = collatz(num)
    return longest

if __name__ == "__main__":
    print(f"Collatz sequence of 13: {collatz(13)}")
    print(f"Collatz sequence of 1: {collatz(1)}")
    print("\n")
    print(f"The number with the longest collatz sequence from 1 to 10'000 (including) is: {longest_collatz()[0]} with a length of: {len(longest_collatz())}")