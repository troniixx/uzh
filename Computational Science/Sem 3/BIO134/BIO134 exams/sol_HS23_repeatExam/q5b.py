#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 5

encoded = 'rtrjsyx ufxx, zsstynhji, zsynq ymjd fwj ltsj.'
#
alphabet 	= 'abcdefghijklmnopqrstuvwxyz'
key 		= 'fghijklmnopqrstuvwxyzabcde'
#

translation = {}

for i in range(len(alphabet)):
    translation[key[i]] = alphabet[i]

decoded = ''
for char in encoded:
    if char in translation:
        decoded += translation[char]
    else:
        decoded += char

print(decoded)


