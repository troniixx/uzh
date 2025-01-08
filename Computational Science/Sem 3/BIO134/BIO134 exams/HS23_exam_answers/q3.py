#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 3

def composition(inputSeq):
    compDic = {}
    for residue in inputSeq:
        if not residue in compDic:
            compDic[residue] = 0
        compDic[residue] += 1
    return compDic

sequence = 'MNREGAPGKSPEEMYIQQKVRVLLMLRKMGSNLTASEEEQGAEDVVMAFSRRRQ'
print(composition(sequence))
