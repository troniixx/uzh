#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 7

primers = ['TCAGCTAGCTCGTAGCTACAGGC', 'CAGGTCACCTGTTAGACTCAGTCG',
           'ACGAGTCGAGCGTAGTCTAC', 'TGAAGTGTGAATAGTACTCACGAG',
           'CGCTCATGTATCATGAGCGCA', 'TGAAGTCGAATAGTTCGACTCA']

complementBases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
IRperPrimer = {}

for primer in primers:

    print('Primer:', primer)
    primerLength = len(primer)
    IRperPrimer[primer] = {}
    
    for anchorPos in range(4, primerLength - 4): 
        
        segmentLength = 0
        spacer = primer[anchorPos - 1: anchorPos + 2].lower()
        currentResult = spacer 
        sequenceIsValid = True
        
        while True:
            currentForward = primer[anchorPos - 2 - segmentLength] 
            currentReverse = primer[anchorPos + 2 + segmentLength]
            if not currentForward == complementBases[currentReverse]: 
                break 
            currentResult = currentForward + currentResult + currentReverse 
            segmentLength += 1
            if segmentLength >= anchorPos: 
                break
            if segmentLength + 2 + anchorPos >= primerLength: 
                break
        
        if segmentLength < 3:
            sequenceIsValid = False
        
        if sequenceIsValid:
            IRperPrimer[primer][anchorPos] = currentResult
            print(" " * (7 + anchorPos - segmentLength), end = "")
            print(currentResult)

    print()
