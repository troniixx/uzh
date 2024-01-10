D = {
    "apple" : 4,
    "banana" : 7,
    "cherry" : 2,
    "date" : 4,
    "elderberry" : 1
    }

def inverse(d):
    inv = {}
    for key, value in d.items():
        if value in inv:
            inv[value].append(key)
        else:
            inv[value] = [key]
    return sorted(inv.items(), key = lambda x: x[0], reverse = True)

print(inverse(D))