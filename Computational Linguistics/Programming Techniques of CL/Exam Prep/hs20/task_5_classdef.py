#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def normalize(s):
    """Return lowercased string where all non-letter characters are deleted

    Unicode characters are should be preserved.
    """
### YOUR Python comments and code start here ###
    result = s
### YOUR Python comments and code end here ###

    return result


# A class for normalized strings
class NormStr(object):

   def __init__(self, s):
### YOUR Python comments and code start here ###
        pass
### YOUR Python comments and code end here ###


   def startswith(self,s):
### YOUR Python comments and code start here ###
        pass
### YOUR Python comments and code end here ###


   def __eq__(self,s):
### YOUR Python comments and code start here ###
        pass
### YOUR Python comments and code end here ###




nstr1 = NormStr('North-West')
nstr2 = NormStr('Northwest')

# Test 1
print("Should print 'True':", nstr1 == nstr2)

# Test 2
print("Should print 'True':", nstr1.startswith('northwe'))

