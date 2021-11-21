s = "aB:cD"

__author__ = "Mert Erol"

print("Start string = " + s)

a, b = s.split(":", 1)

print("String split at : and assigned to new variables;")
print(a)
print(b)

z = a.lower()
y = b.upper()

print(z + ":" + y)