#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 4

# read the data from file
f = open('protoplasts.txt')
lines = f.readlines()
f.close()

# save all datat values to dictionary with timepoints as keys
data = {}
for line in lines:
    linelist = line.strip().split(',')
    timepoint = int(linelist[0])
    length = float(linelist[1])
    width = float(linelist[2])
    
    cellData = [timepoint, length, width, length/width]
    
    if not timepoint in data:
        data[timepoint] = []
    data[timepoint].append(cellData)
 
# print the requested output
print('{:8s}{:8s}{:8s}{:8s}'.format('time', 'length', 'width', 'ratio'))
# # alternative:
# print("time    length  width   ratio   ")

for timepoint in data:
    print('-'*30)
    for cell in data[timepoint]:
        print('{:3d}     {:<8.1f}{:<8.1f}{:<8.1f}'.format(cell[0],cell[1], cell[2], cell[3]))
    