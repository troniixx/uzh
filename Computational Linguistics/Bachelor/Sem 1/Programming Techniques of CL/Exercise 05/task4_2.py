import task4 as t
from sys import argv
import openpyxl as xl
from os.path import basename as bn

def tag_eval(key, test, argv1, argv2):
    #the following two lines are from chatgpt
    key_filename = bn(argv1)
    test_filename = bn(argv2)

    print("CLASSIFICATION EVALUATION STATISTICS")
    print("*"*40+"\n")
    print(f"Key file: {key_filename}\n\t (with reference tags, treated as gold standard)\n")
    print(f"Test file: {test_filename}\n\t (with test tags, possibly wrong)\n\n")
    print("+----------"*8+"+")
    print(t.evaluation_header())
    print("+----------"*8+"+")
    
if __name__ == "__main__":
    key = argv[1]
    test = argv[2]
    t.runner(key, test, key, test)