#!/usr/bin/env python3
__author__ = "Mert Erol"
# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.keywords = keywords
        self.template = template

    def filter(self, msg):
        liste = msg.split(' ')

        for word in liste:
            if word in self.keywords:
                return word.replace(word, self.template)
            
            else: return None



# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
