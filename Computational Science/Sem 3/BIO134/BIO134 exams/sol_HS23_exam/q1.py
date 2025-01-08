#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 1

codons = ['ATG', 'ATT', 'AGG', 'TAC', 'AAG', 'GGA', 'TAG', 'GTG']

sequence = ''
for codon in codons:
    if codon =='TAG':
        break
    sequence += codon 
print(sequence)