print("Question 1")
codons = ['ATG', 'ATT', 'AGG', 'TAC', 'AAG', 'GGA', 'TAG', 'GTG']

s = ""

for cod in codons:
    if cod == "TAG": break
    s += cod

assert s == "ATGATTAGGTACAAGGGA"
print(s)

print("=====================================")
print("Question 2")

tens = [7, 4, 6, 0, 3, 5, 1, 4, 8, 2] 
ones = [3, 1, 5, 2, 6, 2, 9, 8, 4, 1]

sol = []

for i in range(len(tens)):
    sol.append(tens[i]*10 + ones[i])

assert sol == [73, 41, 65, 2, 36, 52, 19, 48, 84, 21]
print(sol)

print("=====================================")
print("Question 3")

def composition(s):
    d = {}
    
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
            
    return d

sequence = 'MNREGAPGKSPEEMYIQQKVRVLLMLRKMGSNLTASEEEQGAEDVVMAFSRRRQ'

assert composition(sequence) == {'M': 5, 'N': 2, 'R': 6, 'E': 7, 'G': 4, 'A': 4, 'P': 2, 'K': 3, 'S': 4, 'Y': 1, 'I': 1, 'Q': 4, 'V': 4, 'L': 4, 'T': 1, 'D': 1, 'F': 1}
print(composition(sequence))

print("=====================================")
print("Question 4")

pi_poem =  'How I wish I could recollect, of circle round, ' 
pi_poem += 'the exact relation Arkimedes unwound.'

tokens = pi_poem.replace(",", "").replace(".", "").split()

pi = 3

print(f"{len(tokens[0])}{tokens[0]:^10}{pi}")
print(".")

for i in range(1, len(tokens)):
    pi += len(tokens[i]) / 10**i
    print(f"{len(tokens[i])} {tokens[i] + (10 - len(tokens[i])) * " "}{pi}")

print("=====================================")
print("Question 5")

import numpy as np

letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
arr_zeros = np.zeros((4, 6))

with open("/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 3/BIO134/BIO134 exams/HS23/densities.csv", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) != 3:
            continue
        
        row_label, col_str, od_str = parts
        
        row = letter_to_index.get(row_label.upper())
        col = int(col_str) - 1
        od = float(od_str)
        
        arr_zeros[row, col] = od
        
print(arr_zeros)
wild_od = np.mean(arr_zeros[0:2, :])
mutant_od = np.mean(arr_zeros[2:4, :])

non_viable_wild = np.sum(arr_zeros[0:2, :] < 0.05)
non_viable_mutant = np.sum(arr_zeros[2:4, :] < 0.05)

print("Wild type mean OD:", wild_od)
print("Mutant mean OD:", mutant_od)

print("Non-viable wild type:", non_viable_wild)
print("Non-viable mutant:", non_viable_mutant)
        

print("=====================================")
print("Question 6")

students = [['11-287-233', 'Justus', 'Meier', 'Justus', 'C'],  
            ['08-609-029', 'Luna Meier', 'Meier', 'Luna', 'A'],  
            ['11-237-784', 'Mhood', 'Hood', 'Maria', 'C'],  
            ['08-169-553', 'Shea_Toby', 'Shea', 'Toby', 'B'],  
            ['08-364-725', 'linC', 'Lin-Schmidt', 'Cason', 'B'],  
            ['08-959-799', 'perez123', 'Perez Sanchez', 'Maria', 'B'],  
            ['09-106-042', 'shayrom', 'Romero', 'Shayna', 'A']] 

results = [['Justus',12,13,5],['Luna Meier',10,11,14],['Shea_Toby',7,6,2],['Mhood',8,10,3],['linC',13,10,15],['perez123',2,3,0], ['shayrom',5,8,4]]

print("\na\n")

def find_best(l):
    best = 0
    name = ""
    for sub in l:
        s = sum(sub[1:])
        if s > best:
            best = s
            s = 0
            name = sub[0]
    
    return best, name
    
best_name = find_best(results)[1]
points = find_best(results)[0]
    
def stalk(stus):
    for stu in stus:
        if best_name in stu:
            return f"{stu[0]} {stu[2]} {stu[3]} {stu[1]} {stu[4]}"
            
print("best student:", points)
print(f"{stalk(students)}")

print("\nb\n")

def find_group(stus, result, group):
    g = []
    
    for sub in stus:
        if group in sub:
            g.append(sub)
            
    return g
    
def summer(full_name, result):
    s = 0
    for res in result:
        if full_name in res:
            for r in res[1:]:
                s += r
        else:
            continue
        
    return s

group_a = find_group(students, results, "A")
group_b = find_group(students, results, "B")
group_c = find_group(students, results, "C")

sums_a = {}
sums_b = {}
sums_c = {}

for sub in group_a:
    sums_a[sub[1]] = summer(sub[1], results)
for sub in group_b:
    sums_b[sub[1]] = summer(sub[1], results)
for sub in group_c:
    sums_c[sub[1]] = summer(sub[1], results)

sums_a_sorted = dict(sorted(sums_a.items(), key=lambda item: item[1]))
sums_b_sorted = dict(sorted(sums_b.items(), key=lambda item: item[1]))
sums_c_sorted = dict(sorted(sums_c.items(), key=lambda item: item[1]))

def look_for_name(name):
    for sub in students:
        if name in sub:
            return f"{sub[2]} {sub[3]}"

def look_for_mat(name):
    for sub in students:
        if name in sub:
            return sub[0]

def part_b():
    print("Group A:")
    for key, value in sums_a_sorted.items():
        print(f"{value} {look_for_mat(key)} {look_for_name(key)}")
    print(f"Group average: {sum(sums_a_sorted.values()) / len(sums_a_sorted)}")
    print("Group B:")
    for key, value in sums_b_sorted.items():
        print(f"{value} {look_for_mat(key)} {look_for_name(key)}")
    print(f"Group average: {sum(sums_b_sorted.values()) / len(sums_b_sorted)}")
    print("Group C:")
    for key, value in sums_c_sorted.items():
        print(f"{value} {look_for_mat(key)} {look_for_name(key)}")
    print(f"Group average: {sum(sums_c_sorted.values()) / len(sums_c_sorted)}")
    
part_b()