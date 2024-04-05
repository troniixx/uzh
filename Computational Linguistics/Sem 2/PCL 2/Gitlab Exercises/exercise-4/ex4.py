# -*- coding: utf-8 -*-
from typing import List
from string import punctuation

REPEAT_COUNT = 10

def repeat_string(text: str, repeat_count: int) -> str:
    return text * repeat_count

def remove_long_tokens(tokens: List[str], max_length: int) -> List[str]:
    sol = [token for token in tokens if len(token) <= max_length]
    return sol

def filter_punctuation(tokens: List[str]) -> List[str]:
    #DONE: implement a function using filter() to remove punctuation
    # Hint: use string.punctuation to get a string of all punctuation characters
    return list(filter(lambda x: x not in punctuation, tokens))
    
def lowercase(tokens: str) -> List[str]:
    #DONE: implement a function using map() to lowercase the tokens
    return list(map(str.lower, tokens))

def length_sort(tokens: List[str]) -> List[str]:
    #DONE: improve the sorting function to sort the tokens by length
    # Hint: an anonymous function could be useful here
    return sorted(tokens, key=len, reverse=True)  # Sort the tokens by length in descending order

def uppercase(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        # Uppercase each string in the list
        uppercased_result = [s.upper() for s in original_result]
        return uppercased_result
    return wrapper

@uppercase
def alphabetical_sort(tokens: List[str]) -> List[str]:
    #DONE: sort the tokens in alphabetical order
    return sorted(tokens)

class Alphabet:
    def __init__(self, letters: str = "abcdefghijklmnopqrstuvwxyz"):
        # Don't change this function
        self.letters = set(letters)
        self.sorted_letters = sorted(self.letters)

    #DONE: make the class iterable by implementing the __iter__ or __getitem__ method
    def __iter__(self):
        return iter(self.sorted_letters)
        
