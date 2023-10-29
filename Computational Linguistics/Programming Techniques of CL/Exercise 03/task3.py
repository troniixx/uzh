#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Mert Erol
# date: 29.10.23

# TASK 3

computercollection = {"Apple II Plus": [1979,"Apple Inc."], "Lisa": [1983,"Apple Inc."], "Canon Cat": [1987, "Canon Inc."], "Tandy 1000": [1984,"Tandy Corporation"], "Apple Newton": [1993, "Apple Inc."]}

# TODO your implementation here

#a
computercollection["IBM 5150"] = [1981, "IBM"]
computercollection["Commodore 64"] = [1982, "Commodore International"]

#b
oldest = next(iter(computercollection))
for key in computercollection:
    if computercollection[key][0] < computercollection[oldest][0]:
        oldest = key
        
print(f"I currently have {len(computercollection)} computers in my collection. The oldest is the {oldest} which was released in {computercollection[oldest][0]}.")

#c
