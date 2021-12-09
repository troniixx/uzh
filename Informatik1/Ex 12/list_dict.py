#!/usr/bin/python3
import string
#uncomment the following line in access {
#from public.data import words #}

#remove these lines in access {
PATH = "enter your path for words.txt here to test on your own device"
with open(PATH) as f:
    words = f.read().splitlines() #}

def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]

def words_containing_string(s):
    return [word for word in words if s in word]

def words_starting_with_character(c):
    return [word for word in words if word.startswith(c)]

def alphabet():
    '''you don't have to solve this one using a comprehension.'''
    return string.ascii_lowercase

def dictionary():
    return {k: v for k, v in zip(alphabet(), [words_starting_with_character(i) for i in alphabet()])}

def censored_words(s):
    return [len(word) * "x" if s in word else word for word in words]


#random tests that can be commented out
print(words_with_length(4))
print(words_containing_string("nig"))
print(words_starting_with_character("g"))
print(alphabet())
print(dictionary())
print(censored_words("me"))