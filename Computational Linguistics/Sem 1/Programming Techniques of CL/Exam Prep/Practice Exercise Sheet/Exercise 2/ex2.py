def grouper(file):
    d = {}
    with open(file, "r") as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                clean = ''.join(ch for ch in word if ch.isalnum())
                if len(clean) in d:
                    d[len(clean)].append(clean)
                else:
                    d[len(clean)] = [clean]
    
    return sorted(d.items(), key = lambda x: len(x), reverse = True)

print(grouper("Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 2/sample.txt"))
