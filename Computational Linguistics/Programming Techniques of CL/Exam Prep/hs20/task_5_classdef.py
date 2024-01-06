#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def normalize(s):
    """Return lowercased string where all non-letter characters are deleted

    Unicode characters are should be preserved.
    """
    return ''.join(char.lower() for char in s if char.isalpha())

class NormStr:
    def __init__(self, s):
    ### YOUR Python comments and code start here ###
        self.normalized = normalize(s)
    ### YOUR Python comments and code end here ###

    def startswith(self, s):
    ### YOUR Python comments and code start here ###
        normalized_s = normalize(s)
        return self.normalized.startswith(normalized_s)
    ### YOUR Python comments and code end here ###

    def __eq__(self, s):
    ### YOUR Python comments and code start here ###
        if isinstance(s, NormStr):
            return self.normalized == s.normalized
        elif isinstance(s, str):
            return self.normalized == normalize(s)
        return False
    ### YOUR Python comments and code end here ###

nstr1 = NormStr('North-West')
nstr2 = NormStr('Northwest')

# Test 1
print("Should print 'True':", nstr1 == nstr2)  # Comparing NormStr with NormStr

# Test 2
print("Should print 'True':", nstr1.startswith('northwe'))  # Testing startswith method
