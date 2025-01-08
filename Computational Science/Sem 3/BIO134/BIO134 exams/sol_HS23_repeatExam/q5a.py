#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 5

encoded = 'rtrjsyx ufxx, zsstynhji, zsynq ymjd fwj ltsj.'
#
alphabet 	= 'abcdefghijklmnopqrstuvwxyz'
key 		= 'fghijklmnopqrstuvwxyzabcde'
#

decoded = ''
for char in encoded:
    if char in key:
        pos = key.index(char)
        decodedChar = alphabet[pos]
    else: 
        decodedChar = char
    decoded += decodedChar

print(decoded)
