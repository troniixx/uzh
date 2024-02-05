def counter(file, word):
    count = 0
    with open(file, "r") as f:
        for line in f:
            count += line.split().count(word)
    
    return count

print(counter("Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 10/sample.txt", "Python"))