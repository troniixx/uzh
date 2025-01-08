#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 3

def meltingTemperature(primer):
    
    gcCount = 0
    atCount = 0
    
    for nt in primer:
        if nt in 'GC':
            gcCount += 1
        elif nt in 'AT':
            atCount += 1
            
    tm = 4*gcCount + 2*atCount
    return tm
        
print(meltingTemperature('TCAGCTAGCTCGTAGCTACAGGC'))
print(meltingTemperature('TGAAGTGTGAATAGTACTCACGAG'))


