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
    print(f"{len(tokens[i])}{tokens[i]:^10}{pi}")

print("=====================================")
print("Question 5")

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

print("a")

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

print("b")

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
    
print(find_group(students, results, "A"))
print(summer("Luna Meier", results))