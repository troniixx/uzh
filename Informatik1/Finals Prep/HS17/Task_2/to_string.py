def stringify(n):
    if n % 2 == 0:
        return str(n) + " is even"
    else: return str(n) + " is odd"

assert stringify(-10) == "-10 is even"
assert stringify(-5) == "-5 is odd"
assert stringify(10) == "10 is even"
assert stringify(5) == "5 is odd"