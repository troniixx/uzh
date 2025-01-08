#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 6

protein = 'MALWRLLPALALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAED'
protein += 'LQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSYQLENYCN'

# create ductionary: keys = amino acids, values = positions of amino acids in protein
positionsPerAminoAcid = {}

for i, aminoAcid in enumerate(protein):
     if not aminoAcid in positionsPerAminoAcid:
         positionsPerAminoAcid[aminoAcid] = []
     positionsPerAminoAcid[aminoAcid].append(i)

# print in required format
for aminoAcid in sorted(positionsPerAminoAcid.keys()):
    positions = positionsPerAminoAcid[aminoAcid]

    # shorter alternative to following loop: append(str(i)) in line 15
    for i in range(len(positions)):
        positions[i] = str(positions[i])
    
    s = '{}:{:3d} x at '.format(aminoAcid, len(positions))
    s += ', '.join(positions)
    print(s)
