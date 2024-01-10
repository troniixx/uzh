def filter_dict(filename):
    with open(filename, "r") as file:
        data = eval(file.read())
    threshold = data["threshold"]
    
    kat = []
    
    for key, value in sorted(data["dictionary"].items(), key = lambda x: x[1], reverse = True):
        if value > threshold:
            kat.append(key)
            
    for key in kat: print(key)
    
filter_dict("Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 8/sample.txt")