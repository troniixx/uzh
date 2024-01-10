def d_printer(file):
    with open(file, "r") as f:
        d = eval(f.read())
    
    sortyboy = sorted(d.items(), key = lambda x: x[1], reverse = True)
    
    for key, value in sortyboy:
        print(f"{key}: {value}")
        
        
d_printer("Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 3/sample.txt")