import part1 as p1
from sys import argv
    
if __name__ == "__main__":
    args = argv
    if len(args) != 4:
        print("Usage: python main.py <hypothesis_file> <reference_file> <ngram>")
        exit(1)
        
    HYP = args[1]
    REF = args[2]
    N = int(args[3])

    print(p1.reader(HYP))
    print(p1.get_ngrams(HYP, N))
    print(p1.get_ngrams(REF, N))

    print(p1.ngram_precision(HYP, REF, N))