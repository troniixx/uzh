#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PCL 1 Exercise 5
Author: PCL Tutors
University of Zurich
Student Names: <your names>

Note: this templates uses Google style Python Docstrings se https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
"""


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

# TODO: Implement command line arguments

# TODO: Process both tabulator-separeted input files (first column TOKEN, second column TAG) and collect statistics

# TODO: Calculate TP/FP/FN/TN values for each tag

# TODO: Calculate the precision, recall and f-score for each tag

# TODO: Print the scores for each tag

# TODO: Print the average scores
