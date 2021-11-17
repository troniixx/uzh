str_freq = {}
def func(str_list):
    str_freq = {}
    for s in str_list:
        str_freq[s] = str_freq[s] + 1
    return str_freq

print(str_freq)