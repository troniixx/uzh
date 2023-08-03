def count_letters(s):
    d = {"upper":0, "lower":0}

    for char in s:
        if char.isalpha():
            if char.islower():
                d["lower"] += 1
            elif char.isupper():
                d["upper"] += 1
            else: continue
        else: continue

    return d
    
d = count_letters("Abc Defg HiJ!")
assert d["upper"] == 4 and d["lower"] == 6
