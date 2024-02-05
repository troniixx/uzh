F1 = "Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 6/file1.txt"
F2 = "Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 6/file2.txt"

def unique(f1, f2):
    d = {"exclusive to file 1": [], "exclusive to file 2": [], "common to both files": []}
    
    l1 = []
    l2 = []
    
    with open(f1, "r") as f_one:
        for line in f_one:
            words = line.strip().split()
            for word in words:
                l1.append(''.join(ch for ch in word if ch.isalnum()))
                
    with open(f2, "r") as f_two:
        for line in f_two:
            words_two = line.strip().split()
            for word in words_two:
                l2.append(''.join(ch for ch in word if ch.isalnum()))
        
    set1 = set(l1)
    set2 = set(l2)
            
    d["exclusive to file 1"] = list(set1 - set2)
    d["exclusive to file 2"] = list(set2 - set1)
    d["common to both files"] = list(set1 & set2)
    
    return d

print(unique(F1, F2))