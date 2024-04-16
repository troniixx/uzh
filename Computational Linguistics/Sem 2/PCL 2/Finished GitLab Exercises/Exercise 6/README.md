# Exercise 6

## Introduction
In this exercise you will write a CLI (Command Line Interface) using `argparse` for calculating the levenshtein distance between two strings.

Given two files, your CLI should be able to:
- Read the content of the files and be capable of appropriate error handling.
- Take the weight of each operation, i.e., insertion, deletion, and substitution as optional arguments. (Default is 1 for all operations)
- Take an optional argument to determine if the levenshtein distance should be calculated on a character or token level. (Default is character level)
- Calculate the levenshtein distance on a line-by-line basis and print the result for each line.

To see what `argparse` has to offer, take a look at its [`documentation`](https://docs.python.org/3/library/argparse.html).

### Evaluation Criteria
This exercise is part of the course assessment and will contribute one point towards your final grade. Ensure you adhere to the following to achieve full marks:
- Independent completion of the exercise.
- Functional implementation utilizing the `argparse` library.
- Well-structured and well-documented code that follows Python best practices.

### Submission
**This is a graded exericse**. Submit your exercise through GitLab by **April 16th at 23:59**. **Late submissions will results in zero points!** Fork the exercise repository to start, and remember to include your name and matriculation number in all files. Add the tutors as 'Reporters' to your repository and finalize your submission by creating a release.
Consult the `instructions.pdf` in OLAT for detailed submission guidelines.

**Note:** To avoid any last-minute issues, it is recommended to submit your work early and verify that the correct files have been uploaded. The zero points rule will apply without exception. If you do encounter any issues, or are unable to submit your work, please contact the tutors immediately.

## Task 1: Write the Argument Parser
You will implement your CLI in the file `levenshtein_cli.py`. You are free to create a class for the CLI, or to solve this exercise with functions. For the first task, you will create the argument parser. The CLI should have the following arguments:
- `--file1`: The path to the first file.
- `--file2`: The path to the second file.
- `--insertion`: The weight of the insertion operation. Default is 1.
- `--deletion`: The weight of the deletion operation. Default is 1.
- `--substitution`: The weight of the substitution operation. Default is 1.
- `--tokenize`: The levenshtein distance is calculated on character level by default. When the script is called with the `--tokenize` flag (hint: use `action='store_true'`), the lines will be tokenized and the levenshtein distance is calculated on token level.

Make sure the parser has a description and the arguments the necessary properties such as type, default, help message, etc.

## Task 2: Expand the Levenshtein Distance Function
In `levenshtein_base.py` you will find the function `levenshtein` which calculates the levenshtein distance with all operations having the same weight. Adapt this function so that it takes custom weights for the operations as additional arguments.

`test_levenshtein.py` contains some tests for the `levenshtein` function. Use these tests to verify that your adapted function works correctly. **Note:** The given tests are not exhaustive, you should write additional tests to ensure the correctness of your implementation.

## Task 3: Implement the rest of the CLI
Implement the rest of the CLI so that the functionality described in the introduction is fulfilled. You can use the text files in the `samples` folder and write your own tests to verify the correctness of your CLI implementation.


An example of how the CLI should be used is shown below:
```bash
python levenshtein_cli.py --file1 samples/text1.txt --file2 samples/text2.txt --insertion 1 --deletion 1 --substitution 1
```

Consider the following table. The lines in the columns `file1` and `file2` represent the contents of the files line by line. The column `levenshtein distance` represents the scores your program should output. In this case, we computed the character-based levenshtein distance with a weight of 1 for insertion, deletion and substitution. **Note**: You do not need to output a table or format the output prettily, printing the scores line by line is enough.

| file1 | file2 | levenshtein distance |
| ----- | ----- | ---- |
| Hello | hello | 1 |
| w     | world |  4 |
| !     | .     |  1 |


For the text preprocessing, first read the input files line by line.
- For character-based levenshtein distance, no further preprocessing is needed.
- For token-based levenshtein distance, **remove any punctuation besides apostrophes from contractions**. The text should then be split into tokens.

### Error Handling
Python and the `argparse` library already provide some error handling. You may also write additional code to handle errors. Make sure your script will terminate and display a meaningful error message in the following cases:
- Missing arguments
- Incorrect types of arguments
- Incorrect values of arguments (for example, the weights should never be negative numbers. Both `int` and `float` are valid, and a weight of `0` is also allowed.)
- The two input files contain different numbers of lines.

We recommend that you write additional tests to verify that your error handling works correctly, it will also make it easier to debug your code.