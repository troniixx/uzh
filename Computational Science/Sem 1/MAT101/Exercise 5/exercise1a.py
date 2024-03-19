def digital_root(n):
    if n < 1 or not isinstance(n, int):
        return ValueError("n must be a positive integer")
    
    num_str = str(n)
    
    # Sum up the digits
    digit_sum = 0
    for digit in num_str:
        digit_sum += int(digit)
    
    # If the sum is greater than 9, repeat the process with the sum
    if digit_sum > 9:
        digit_sum = digital_root(digit_sum)
    
    return digit_sum

"""
I used this for testing:
For part b) look at the file "exercise1b.py"

if __name__ == "__main__":
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))
    
"""