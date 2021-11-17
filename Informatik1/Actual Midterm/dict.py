a = (1, [])

def func(a, lst):
    a[0] = lst + lst
    a += [(3, 4), lst]
    return a

print(func(a,[]))