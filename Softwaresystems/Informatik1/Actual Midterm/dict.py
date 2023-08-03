a = (1, [])
str_freq = {}

def func(a, lst):
    a[0] = lst + lst
    a += [(3, 4), lst]
    return a

def func(str_list):
    str_freq = {}
    for s in str_list:
        str_freq[s] = str_freq[s] + 1
    return str_freq