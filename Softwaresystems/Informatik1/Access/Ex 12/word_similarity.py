#!/usr/bin/env python3

import random
from difflib import SequenceMatcher
from math import floor
class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def is_similar(self, a, b, threshold):
        if SequenceMatcher(None, a, b).ratio() > threshold:
            return True
        else: return False

    def word_selection(self):
        words = self.find_words_with_right_size()
        random.shuffle(words)
        pool = floor(self.num_words/3)
        selected = random.choice(words[:pool])
        pool2 = words[pool:]
        res = [selected]

        while len(res) < self.num_words:
            t = random.choice(pool2)
            if t not in res and self.is_similar(selected, t, 0.4):
                res.append(t)
        # TODO: instead of returning a random sample of words, use the strategy described in task 2
        return res
