#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PCL 1 Exercise 5
Author: PCL Tutors
University of Zurich
Student Names: Mert Erol

Note: this templates uses Google style Python Docstrings se https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
"""

from sys import argv

def evaluation_header():
    """
    Return the header line of the output.
    Returns:
        str: the formatted head of the confusion table
    """
    
    return f"{'-' * 60} \n{'tag':^10} | {'present':^10} | {'found':^10} | {'wrong':^10} | {'missed':^10} | {'prec':^10} | {'recal':^10} | {'f-mea':^10} \n{'-' * 60}"


def format_evaluation_line(tag, present, found, wrong, missed, prec, recal, f_mea):
    """
    Return the formatted evaluation results for a single tag.
    Args:
        tag (str): POS tag
        present (int): number of occurrences of the tag in the key file
        found (int): number of occurrences of the tag in the system output
        wrong (int): number of wrong occurrences of the tag in the system output
        missed (int): number of occurences of the tag from the key file missing in the system output
        prec (float): precision of the tag
        recal (float): recall of the tag
        f_mea (float): f-measure of the tag
    Returns:
        str: the formatted row for the tag of the confusion table
    """

    return f"{tag:^10} | {present:^10} | {found:^10} | {wrong:^10} | {missed:^10} | {prec:^10.2f} | {recal:^10.2f} | {f_mea:^10.2f}"

# DONE: Check if the key and test files are identical, if not print an error message in runner() and exit the program
def sanity_check(key, test):
    with open(key, "r", encoding = "utf-8") as key_file, open(test, "r", encoding = "utf-8") as test_file:
        content_key = set(line.split("\t")[0] for line in key_file)
        content_test = set(line.split("\t")[0] for line in test_file)

    if content_key == content_test:
        return True
    else:
        return False


# DONE: Process both tabulator-separeted input files (first column TOKEN, second column TAG) and collect statistics
# I split the function into two parts, one for key and one for test file. I did this because it was easier for me to test&debug the code.
# and ofc bc i could then just copy paste it :) 
def key_collect(key):
    stats_key = {}
    with open(key, "r", encoding = "utf-8") as key_file:
        for line in key_file:
            line = line.strip()
            parts = line.split("\t")

            if len(parts) == 2:
                token, tag = parts
                tag = tag.strip()
                if tag in stats_key:
                    stats_key[tag] += 1
                else:
                    stats_key[tag] = 1
                        
    return stats_key

def test_collect(test):
    stats_test = {}
    
    with open(test, 'r') as test_file:
        for line in test_file:
            line = line.strip()
            parts = line.split("\t")

            if len(parts) == 2:
                token, tag = parts
                tag = tag.strip()
                if tag in stats_test:
                    stats_test[tag] += 1
                else:
                    stats_test[tag] = 1

    return stats_test

def collector(key, test):

    stats_key = key_collect(key)
    stats_test = test_collect(test)
                
    return stats_key, stats_test

# DONE: Calculate TP/FP/FN/TN values for each tag
def confusion_matrix(key, test):
    stats_key, stats_test = collector(key, test)
    tag_counts = {tag: {'TP': 0, 'FP': 0, 'FN': 0, 'TN': 0} for tag in set(stats_key) | set(stats_test)} #got this idea of using dicts from ChatGPT
    #query i used: i sent both .tts files and asked if there is a way of categorizing the tags into TP, FP, FN, TN. The awnser was to use a dict to keep track of the tags while being time/space efficient

    with open(key, "r", encoding="utf-8") as key_file, open(test, "r", encoding="utf-8") as test_file:
        #combining the two files into one list to iterate over them at the same time, thank god for stackoverflow 
        for key_line, test_line in zip(key_file, test_file):
            #strip the lines to remove the \n at the end and split them into parts, looks something like this: ['token', 'tag']
            key_parts = key_line.strip().split("\t")
            test_parts = test_line.strip().split("\t")

            #if the length of the parts is 2, assign the token and tag to the variables. this is making sure that it is comparable
            if len(key_parts) == 2 and len(test_parts) == 2:
                key_tag = key_parts[1].strip()
                test_tag = test_parts[1].strip()

                #classifying each tag from the files into TP, FP, FN, TN
                for tag in tag_counts.keys():
                    if key_tag == test_tag == tag:
                        tag_counts[tag]['TP'] += 1
                    elif key_tag == tag and test_tag != tag:
                        tag_counts[tag]['FN'] += 1
                    elif key_tag != tag and test_tag == tag:
                        tag_counts[tag]['FP'] += 1
                    else:
                        tag_counts[tag]['TN'] += 1
    
    return tag_counts

# TODO: Calculate the precision, recall and f-score for each tag
def values_calc(key, test):
    tag_list = confusion_matrix(key, test)
    values_each = {}

    
    
    return values_each

# TODO: Print the scores for each tag
def printer_score(key, test):
    prec, recal, f_mea = values_calc(key, test)
    
    
    print("x")

# TODO: Print the average scores
def printer_avg(key, test):
    pass

# DONE: runner function to keep the main nice and clean
def runner(key, test):
    if not sanity_check(key, test):
        print("The files are not identical.")
        return
    
    print(confusion_matrix(key, test))
    #evaluation_header()
    #format_evaluation_line()
    #printer_score(key, test)
    #printer_avg(key, test)


if __name__ == '__main__':
    #key, test laptop
    #key = "/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Exercise 05/test.tts"
    #test = "/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Exercise 05/result.tts"
    
    #key, test, nmsg
    key = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Exercise 05/test.tts"
    test = "/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Exercise 05/result.tts"

    # DONE: Implement command line arguments to get key and test
    #key = argv[1]
    #test = argv[2]
    runner(key, test)
    

