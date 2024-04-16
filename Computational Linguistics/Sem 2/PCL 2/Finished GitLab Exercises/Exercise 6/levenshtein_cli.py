# Student Name: Mert Erol
# Matriculation Number: 20-915-245
# Environment: Python 3.12.3
# Encoding: UTF-8

from levenshtein_base import levenshtein
import argparse
import sys

# DONE: Create a functioning Command-Line Interface
def float_or_int(value: str) -> int | float | argparse.ArgumentTypeError:
    """
    function to convert a string to a float or int if possible and raise an error if not
    
    :param value: str
    
    :return: int | float | Error
    """
    try:
        # Try converting to int first
        ivalue = int(value)
        return ivalue
    except ValueError:
        try:
            # Try converting to float if int fails
            fvalue = float(value)
            return fvalue
        except ValueError:
            raise argparse.ArgumentTypeError(f"Invalid numerical value: {value}")
        
def create_parser() -> argparse.ArgumentParser:
    """
    function to create an argument parser for the CLI and return it
    
    :return: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Levenshtein Distance Calculator on character Level or token Level")
    parser.add_argument("-f1", "--file1", help = "Path to the first file", type = str, required = True)
    parser.add_argument("-f2", "--file2", help = "Path to the second file", type = str, required = True)
    parser.add_argument("-i", "--insertion", help = "Set cost of insertion operation", type = float_or_int, default = 1)
    parser.add_argument("-d", "--deletion", help = "Set cost of deletion operation", type = float_or_int, default = 1)
    parser.add_argument("-s", "--substitution", help = "Set cost of substitution operation", type = float_or_int, default = 1)
    parser.add_argument("-t", "--tokenize", help = "Tokenize the input strings and calculate levenshtein distance on token level", action = "store_true")
    
    return parser

def main():
    """
    main function to run the CLI and calculate the levenshtein distance between the lines of two files passed as arguments
    returns the levenshtein distance per line or an error message if the files are not found
    """
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        with open(args.file1, "r") as file1, open(args.file2, "r") as file2:
            i = 1 # line counter
            # iterate over the lines of the files
            for line1, line2 in zip(file1, file2):
                line1 = line1.strip()
                line2 = line2.strip()
                
                # calculate levenshtein distance and print the result per line
                distance = levenshtein(line1, line2, args.insertion, args.deletion, args.substitution, args.tokenize)
                print(f"Levenshtein distance between line {i}: {distance}")
                i += 1
    # handle file not found error
    except FileNotFoundError:
        print("File not found. Exiting...", file=sys.stderr) # print error message to stderr (used in test cases)
        sys.exit(1) # exit with status code 1 (used in test cases)

if __name__ == "__main__":
    main()
