def cat(file):
    d = {}
    with open(file, "r") as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                first = word[0]
                if first in d:
                    d[first].append(word)
                else:
                    d[first] = [word]
    for letter, words in sorted(d.items(), key = lambda x: len(x[1]), reverse = True):
        print(f"{letter}: {words}")
        
cat("Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 4/sample.txt")