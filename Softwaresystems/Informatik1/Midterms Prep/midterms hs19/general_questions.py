g = 0

for n in [1, 2, 3.0, 4.0]:
    if n%2:
        g += n
    break #jump out of function as soon as one value mod2 = 1 => 1

print(g)


a = [1, 2, 3]
b = [1, 2, 3]
c = b
print(c)
if a == c:
    j = a is c
else:
    j = b == c
print(j)