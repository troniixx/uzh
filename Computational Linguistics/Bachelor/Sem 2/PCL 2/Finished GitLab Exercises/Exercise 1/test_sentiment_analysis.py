#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_sentiment_analysis.py

# University of Zurich
# Department of Computational Linguistics

# Authors: Mert Erol
# Matriculation Numbers: 20-915-245


import pytest
from sentiment_analysis import tokenize, remove_stopwords, analyse_sentiment, pretty_print


def test_tokenize():
    # DONE: 3 own test assertions
    s1 = 'The cat slept peacefully in the afternoon sun.'
    e1 = ['The', 'cat', 'slept', 'peacefully', 'in', 'the', 'afternoon', 'sun', '.']
    assert tokenize(s1) == e1
    
    s2 = 'My students are the best, they are always eager to learn.'
    e2 = ['My', 'students', 'are', 'the', 'best', ',', 'they', 'are', 'always', 'eager', 'to', 'learn', '.']
    assert tokenize(s2) == e2
    
    s3 = 'The rain was relentless and the picnic was ruined.'
    e3 = ['The', 'rain', 'was', 'relentless', 'and', 'the', 'picnic', 'was', 'ruined', '.']
    assert tokenize(s3) == e3


def test_remove_stopwords():
    # DONE: 3 own test assertions
    s1 = ['The', 'cat', 'slept', 'peacefully', 'in', 'the', 'afternoon', 'sun', '.']
    e1 = ['cat', 'slept', 'peacefully', 'afternoon', 'sun', '.']
    assert remove_stopwords(s1) == e1
    
    s2 = ['My', 'students', 'are', 'the', 'best', ',', 'they', 'are', 'always', 'eager', 'to', 'learn', '.']
    e2 = ['students', 'best', ',', 'always', 'eager', 'learn', '.']
    assert remove_stopwords(s2) == e2
    
    s3 = ['The', 'rain', 'was', 'relentless', 'and', 'the', 'picnic', 'was', 'ruined', '.']
    e3 = ['rain', 'relentless', 'picnic', 'ruined', '.']
    assert remove_stopwords(s3) == e3


def test_analyse_sentiment():
    with open('sentiment_words/positive-words.txt', 'r') as pos_file, open('sentiment_words/negative-words.txt', 'r') as neg_file:
        pos_set = {line.strip() for line in pos_file}
        neg_set = {line.strip() for line in neg_file}
    
    # normal case
    tokens_1 = ['like', 'nonsense', ',', 'wakes', 'brain', 'cells', '.', 'Fantasy', 'necessary', 'ingredient', 'living', '.']
    expected_1 = (1, 1, ['like'], ['nonsense'])
    assert analyse_sentiment(tokens_1, pos_set, neg_set) == expected_1

    # empty list as input
    tokens_2 = []
    expected_2 = (0, 0, [], [])
    assert analyse_sentiment(tokens_2, pos_set, neg_set) == expected_2

    # no sentiment words in the list
    tokens_3 = ['test', 'cover', 'corner', 'cases', '!']
    expected_3 = (0, 0, [], [])
    assert analyse_sentiment(tokens_3, pos_set, neg_set) == expected_3


def test_pretty_print(capsys):
    pretty_print("Despite the rain, their picnic was filled with love and warmth, creating cherished memories.", 3, 0, ['love', 'warmth', 'cherished'], [])
    captured = capsys.readouterr()
    expected_output_1 = """Despite the rain, their picnic was filled with love and warmth, creating cherished memories.
\nPositive words count: 3\tPositive words: ['love', 'warmth', 'cherished']
Negative words count: 0\tNegative words: []
The sentiment of this quote is: POSITIVE
----------------------------------------
"""
    assert captured.out == expected_output_1

    pretty_print("The cat slept peacefully in the afternoon sun.", 0, 0, [], [])
    captured = capsys.readouterr()
    expected_output_2 = """The cat slept peacefully in the afternoon sun.
\nPositive words count: 0\tPositive words: []
Negative words count: 0\tNegative words: []
The sentiment of this quote is: NEUTRAL
----------------------------------------
"""
    assert captured.out == expected_output_2

    pretty_print("The rain was relentless and the picnic was ruined.", 0, 2, [], ['relentless', 'ruined'])
    captured = capsys.readouterr()
    expected_output_3 = """The rain was relentless and the picnic was ruined.
\nPositive words count: 0\tPositive words: []
Negative words count: 2\tNegative words: ['relentless', 'ruined']
The sentiment of this quote is: NEGATIVE
----------------------------------------
"""
    assert captured.out == expected_output_3
