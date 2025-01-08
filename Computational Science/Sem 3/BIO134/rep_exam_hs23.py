print("Question 1")
genotypes = [1, 4, 2, 1, 3, 4, 3, 4, 1, 4, 3, 2, 4, 4, 2]

counter = 0

for i in genotypes:
    if i < 4:
        counter += 1
        
print(counter)
print(counter/len(genotypes))

print("Question 2")

codons = ['TCG', 'ATG', 'ATT', 'TCT', 'GAC', 'ATG', 'GCG',
'TCA', 'ATG', 'GTA', 'CTC', 'GCG', 'GAG']

sol = {}

for idx, item in enumerate(codons):
    if item in sol:
        sol[item].append(idx)
    else:
        sol[item] = []
        sol[item].append(idx)
        
print(sol)

print("Question 3")

def meltingTemperature(s):
    cnt_g = 0
    cnt_c = 0
    cnt_a = 0
    cnt_t = 0
    
    for char in s:
        if char == "G": cnt_g += 1
        elif char == "C": cnt_c += 1
        elif char == "A": cnt_a += 1
        else: cnt_t += 1
    
    t = 4 * (cnt_g + cnt_c) + 2 * (cnt_a + cnt_t)
    
    return t
    
print(meltingTemperature('TCAGCTAGCTCGTAGCTACAGGC'))
print(meltingTemperature('TGAAGTGTGAATAGTACTCACGAG'))

print("Questions 4")


print("Question 5")

encoded = 'rtrjsyx ufxx, zsstynhji, zsynq ymjd fwj ltsj.'

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'fghijklmnopqrstuvwxyzabcde'

sol = ""

for char in encoded:
    if not char.isalpha():
        sol += char
    for c in key:
        if char == c:
            sol += alphabet[key.index(c)]
            
print(sol)

print("Question 6")

import numpy as np

def count_neighbors(binary):
    rows, cols = binary.shape
    result = np.zeros_like(binary)
    
    for i in range(rows):
        for j in range(cols):
            # Define neighbor boundaries
            row_start = max(0, i-1)
            row_end = min(rows, i+2)
            col_start = max(0, j-1)
            col_end = min(cols, j+2)
            
            neighbor_sum = binary[row_start:row_end, col_start:col_end].sum()
            if binary[i,j] == 1:
                neighbor_sum -= 1
                
            result[i,j] = neighbor_sum
            
    return result

binary = np.zeros((6,8), dtype=int)
binary[0,7] = 1
binary[5,3] = 1
binary[3,1:4] = 1

result = count_neighbors(binary)
print(result)