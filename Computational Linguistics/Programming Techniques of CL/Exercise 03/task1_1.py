#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Mert Erol
# date: 27.10.23

# TASK 1.1

# list of ingredients

aquarium = ['pebbles','castle','plants','filter','big_rock','small_rock','castle','goldfish']
print(aquarium)
# TODO your implementation here
#a
castle = aquarium.count('castle')
print(castle)

#b
counter = 0
for i in range(0, len(aquarium)):
    if aquarium[i] == 'castle':
        counter += 1
    if counter == 2:
        aquarium.pop(i)
        break
        
        
print(aquarium)
        
#c
aquarium.append("golfball")
print(aquarium)

#d
aquarium.insert(5, "cat")
print(aquarium)

#e
print(aquarium.index("goldfish"))

#f
for item in aquarium:
    if item == "goldfish":
        aquarium[aquarium.index(item)] = "oh no"
print(aquarium)

#g
print(len(aquarium))

#h
print(aquarium)

#i
terrarium = []

#j
terrarium.append(aquarium[5])

#k
terrarium.append("python")

#l
print("Task l: ")
sorted(terrarium)
print(terrarium)
print(aquarium)
