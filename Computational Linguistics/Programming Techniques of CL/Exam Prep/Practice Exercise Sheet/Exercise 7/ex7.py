def freq_counter(filename):
    d = {}
    with open(filename, "r") as f:
        for line in f:
            for char in line:
                if char.lower() in d:
                    d[char.lower()] += 1
                else:
                    d[char.lower()] = 1
                    
    return sorted(d.items(), key = lambda x: x[1], reverse = True)

print(freq_counter("Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 7/sample.txt"))