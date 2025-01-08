#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 4

f = open('protoplasts.txt')
lines = f.readlines()
f.close()

currentTimepoint = None

print('{:8s}{:8s}{:8s}{:8s}'.format('time', 'length', 'width', 'ratio'))
# # alternative:
# print("time    length  width   ratio   ")

for line in lines:
    
    linelist = line.strip().split(',')
    
    timepoint = int(linelist[0])
    length = float(linelist[1])
    width = float(linelist[2])
    ratio = length/width
    
    if timepoint != currentTimepoint:
        print('-'*30)
        currentTimepoint = timepoint
    
    print('{:3d}     {:<8.1f}{:<8.1f}{:<8.1f}'.format(timepoint, length, width, ratio))
    