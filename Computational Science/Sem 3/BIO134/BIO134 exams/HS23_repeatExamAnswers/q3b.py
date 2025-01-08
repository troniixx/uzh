#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 3

def meltingTemperature(primer):

    countsPerLetter = {'A': 0, 'C': 0, 'T': 0, 'G': 0}

    for letter in primer:
        countsPerLetter[letter] += 1

    tm = 4 * (countsPerLetter['G'] + countsPerLetter['C']) + 2 * (countsPerLetter['A'] + countsPerLetter['T'])
    return tm

print(meltingTemperature('TCAGCTAGCTCGTAGCTACAGGC'))
print(meltingTemperature('TGAAGTGTGAATAGTACTCACGAG'))



