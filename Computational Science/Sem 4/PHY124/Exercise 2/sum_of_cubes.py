res = []

n = 20

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            for d in range(1, n+1):
                if a**3 + b**3 + c**3 == d**3:
                    res.append((a, b, c, d))

print(res)