from collections import Counter

def count_chars(s):
    d = {}

    for char in s:
        d[char] = d.get(char, 0)+1

    return d


print(count_chars(""))
print(count_chars("aA ."))
print(count_chars("abbCaabb"))