#!/usr/bin/env python3
import re
# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.


class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = sorted(keywords, key=len, reverse=True)
        self.__template = template

    def __clean(self, word):
        badword = False
        rest = ['', '']
        for i in self.__keywords:
            if i.lower() in word.lower():
                rest = re.split(i, word, flags=re.IGNORECASE)
                badword = True
                break
        if badword:    
            factor = len(word) // len(self.__template) + 1
            clean = factor * self.__template
            clean = rest[0] + clean[:len(word)] + rest[1]
            return clean
        else: return word

    def filter(self, msg):
        for word in msg.split():
            msg = msg.replace(word, self.__clean(word))
        return msg

if __name__ == '__main__':
    f = ProfanityFilter(["duck", "Shot", "batch", "mastard"], "?#$")
    #offensive_msg = "absHOtc DebATChfghi AaaMaStard jklMnoDUCK duck sHOt"
    offensive_msg = "xxduckxx"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)