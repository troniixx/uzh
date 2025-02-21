print("Question 1:")

seq = 'TAATTTCTGACNATGGCGTCAATGGTACTCGCGNNGAG'

for char in seq:
    if char == "N":
        break
    print(char)
    
#this is a test

print("=====================================")
print("Question 2:")

original = ['my', 'care', 'is', 'loss', 'of', 'care', 'by', 'old', 'care', 'done']

seen = []
sol = []

for item in original:
    if item in seen:
        continue
    seen.append(item)
    sol.append(item)
    
print(sol)

print("=====================================")
print("Question 3:")

import numpy as np
np.random.seed(1)

def guessing(i, j):
    a = 1
    
    while True:
        n = np.random.randint(1, 7)
        if i == n:
            return 1, n, a
        elif j == n:
            return 2, n, a
        else:
            a += 1

w, n, a = guessing(3,4) # winner, number, attempt 
print('Player {} won! {} was rolled with the {}. roll.'.format(w, n, a))

print("=====================================")
print("Question 4:")

items = [['fly', 'bat', 'eagle'], ['hut', 'barn', 'villa', 'castle']]
sol = []

def reverser(l):
    rev = []
    
    for i in range(len(l)-1, -1, -1):
        rev.append(l[i])
        
    return rev
    
for sub in items:
    sol.append(reverser(sub))
    
print(sol)

print("=====================================")
print("Question 5:")
protein = 'MALWRLLPALALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAED' 
protein += 'LQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSYQLENYCN'

def printer(l):
    s = ""
    for i in l[:-1]:
        s += str(i) + ", "
    s += str(l[-1])
    
    return s

chars = {}

for idx, char in enumerate(protein):
    if char not in chars:
        chars[char] = []
        chars[char].append(idx)
    else:
        chars[char].append(idx)
    
chars = dict(sorted(chars.items()))

for char in chars:
    print(f"{char}: {len(chars[char]):>3} x at {printer(chars[char])}")

print("=====================================")
print("Question 6:")

print("=====================================")
print("Question 7:")
