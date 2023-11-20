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

# TODO: Calculate TP/FP/FN/TN values for each tag
def confusion_matrix(key, test):
    stats_key, stats_test = collector(key, test)
    tp, fp, fn, tn = 0, 0, 0, 0
    
    #need to rewrite this to print for each tags
    return tp, fp, fn, tn

# TODO: Calculate the precision, recall and f-score for each tag
def values_calc(key, test):
    tp, fp, fn, tn = confusion_matrix(key, test)
    prec, recal, f_mea = 0, 0, 0
    
    #need to rewrite this to print for each tags
    return prec, recal, f_mea

# TODO: Print the scores for each tag
def printer_score(key, test):
    prec, recal, f_mea = values_calc(key, test)
    
    
    print("x")

# TODO: Print the average scores
def printer_avg(key, test):
    pass

def runner(key, test):
    if not sanity_check(key, test):
        print("The files are not identical.")
        return
    
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

    # DONE: Implement command line arguments
    #key = argv[1]
    #test = argv[2]
    runner(key, test)
    
