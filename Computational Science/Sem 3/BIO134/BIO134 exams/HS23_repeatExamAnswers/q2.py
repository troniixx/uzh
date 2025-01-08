#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 2

codons = ['TCG', 'ATG', 'ATT', 'TCT', 'GAC', 'ATG', 'GCG', 'TCA', 'ATG', 'GTA', 'CTC', 'GCG', 'GAG']

codonPositions = {}

for i, codon in enumerate(codons):
    if not codon in codonPositions:
        codonPositions[codon] = []
    codonPositions[codon].append(i)

print(codonPositions)
