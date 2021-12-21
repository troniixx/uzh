symbols = ["a", "b", "c", "d", "e", "f", "g", 
"A", "B", "C", "D", "E", "F", "G",
"h", "i", "j", "k", "l", "m", "n",
"H", "I", "J", "K", "L", "M", "N",
"o", "p", "q", "r", "s", "t", "u",
"O", "P", "Q", "R", "S", "T", "U",
"v", "w", "x", "y", "z", ".", "?",
"V", "W", "X", "Y", "Z", " ", "!"]

indices = [3, 64, 21, 30, 27, 14, 28]
s = ""
for idx in indices:
    if idx < 10:
        s += str(idx)
    else:
        s += symbols[idx-10]

print(s)