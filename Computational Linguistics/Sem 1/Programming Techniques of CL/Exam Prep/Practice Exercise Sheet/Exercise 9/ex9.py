def sum_values(filename):
    with open(filename, "r") as file:
        d = eval(file.read())
    
    total = 0
    
    for key, value in sorted(d.items(), key = lambda x: x[1], reverse = True):
        total += value
        
    return total

print(sum_values("Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 9/sample.txt"))