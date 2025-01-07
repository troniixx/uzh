students = [['11-287-233', 'Justus', 'Meier', 'Justus', 'C'],
['08-609-029', 'Luna Meier', 'Meier', 'Luna', 'A'],
['11-237-784', 'Mhood', 'Hood', 'Maria', 'C'],
['08-169-553', 'Shea_Toby', 'Shea', 'Toby', 'B'],
['08-364-725', 'linC', 'Lin-Schmidt', 'Cason', 'B'],
['08-959-799', 'perez123', 'Perez Sanchez', 'Maria', 'B'],
['09-106-042', 'shayrom', 'Romero', 'Shayna', 'A']]

results = [['Justus',12,13,5], ['Luna Meier',10,11,14], ['Shea_Toby',7,6,2],
['Mhood',8,10,3], ['linC',13,10,15], ['perez123',2,3,0], ['shayrom',5,8,4]]

def find_best(l):
    score = 0
    best = 0
    name = ""
    
    for sub in l:
        for item in sub[1:]:
            score += item
            
            if score > best:
                best = score
                score = 0
                name = sub[0]
    
    
    return name

def summer(l, best_stu):
    summe = 0
    
    for sub in l:
        if best_stu in sub:
            for i in sub:
                if isinstance(i, int):
                    summe += i
                    
    return summe
    
def summer_specific(l, name):
    summe = 0
    
    for sub in l:
        if name in sub:
            for i in sub:
                if isinstance(i, int):
                    summe += i
                    
    return summe

def stalk(stus):
    out = ""
    best_stu = find_best(results)
    
    for sub in stus:
        if best_stu in sub:
            out += f"{str(sub[0])} "
            out += f"{str(sub[2])} "
            out += f"{str(sub[3])} "
            out += f"{str(sub[1])} "
            out += f"{str(sub[4])}"
    
    return out   

print("a)")
print(f"best student: {summer(results, find_best(results))} points")
print(f"{stalk(students)}")

print("b)")

