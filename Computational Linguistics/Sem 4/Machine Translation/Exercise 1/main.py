import part1 as p1
    
if __name__ == "__main__":
    HYP = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Sem 4/Machine Translation/Exercise 1/test_files/test_hypothesis.txt"
    REF = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Sem 4/Machine Translation/Exercise 1/test_files/test_reference.txt"

    print(p1.reader(HYP))
    print(p1.get_ngrams(HYP, 3))
    print(p1.get_ngrams(REF, 3))

    print(p1.ngram_precision(HYP, REF, 2))