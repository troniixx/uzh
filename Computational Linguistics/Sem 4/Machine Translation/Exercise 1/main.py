import part1 as p1
    
if __name__ == "__main__":
    print(p1.reader("/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Sem 4/Machine Translation/Exercise 1/test_files/test_reference.txt"))
    print(p1.get_ngrams("/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Sem 4/Machine Translation/Exercise 1/test_files/test_reference.txt", 3))