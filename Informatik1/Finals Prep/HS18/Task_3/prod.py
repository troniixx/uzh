def prod(x, y):
    res = 0
    if y == 0: 
        return res
    res = x+x
    return res + prod(x, y-2)

assert prod(2, 0) == 0
assert prod(5, 2) == 10
assert prod(69, 420) == 28980