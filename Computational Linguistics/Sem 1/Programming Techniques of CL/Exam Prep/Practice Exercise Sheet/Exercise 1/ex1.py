def word_count(filename):
    word_dict = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    
    print(word_dict)
    
word_count("Computational Linguistics/Programming Techniques of CL/Exam Prep/Practice Exercise Sheet/Exercise 1/sample.txt")