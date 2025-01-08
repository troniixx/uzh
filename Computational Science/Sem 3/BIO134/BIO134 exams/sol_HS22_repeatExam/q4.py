#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 4

items = [['fly', 'bat', 'eagle'], ['hut', 'barn', 'villa', 'castle']]

reversedItems = []

for sublist in items:
    reversedSublist = []
    for i in range(len(sublist)-1,-1,-1): # again only 1 of many possibilities!
        reversedSublist.append(sublist[i])
    reversedItems.append(reversedSublist)
print(reversedItems)