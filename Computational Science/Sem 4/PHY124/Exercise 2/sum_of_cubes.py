res = []

n = 100

for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            for d in range(n+1):
                if a**3 + b**3 + c**3 == d**3:
                    res.append((a, b, c, d))

print(res)