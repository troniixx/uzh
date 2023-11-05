#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Mert Erol
# date: 29.10.23

# TASK 3

computercollection = {"Apple II Plus": [1979,"Apple Inc."], "Lisa": [1983,"Apple Inc."], "Canon Cat": [1987, "Canon Inc."], "Tandy 1000": [1984,"Tandy Corporation"], "Apple Newton": [1993, "Apple Inc."]}

# TODO your implementation here

#b
def oldest_boy(dicti):
    oldest_year = float('inf')
    oldest_computer = None
    for computer, value in dicti.items():
        if value[0] < oldest_year:
            oldest_year = value[0]
            oldest_computer = computer

    return f"I currently have {len(dicti)} computers in my collection. The oldest is the {oldest_computer} which was released in {oldest_year}.\n"

#c part 1: sort dictionary by company
def get_company(dicti):
    return dicti[1][1]

def sorty_boy(dicti):
    sorted_dicti = dict(sorted(dicti.items(), key = get_company))
    
    output = ""
    
    for computer, value in sorted_dicti.items():
        company = value[1]
        output += f"{company} {computer}\n"

    return output

#c part 2: 
# return ’The company I own most machines of is [company name]: I own [number] computers by them.’
def num_machines(dicti):
    sorted_d = dict(sorted(dicti.items(), key = get_company))
    
    counts = {}
    
    for company, value in sorted_d.items():
        company_name = value[1]
        if company_name in counts:
            counts[company_name] += 1
        else:
            counts[company_name] = 1

    most_owned_company = max(counts, key=counts.get)
    most_owned_count = counts[most_owned_company]

    return f"The company I own most machines of is {most_owned_company}: I own {most_owned_count} computers by them."
    
if __name__ == "__main__":
    #a
    computercollection["IBM 5150"] = [1981, "IBM"]
    computercollection["Commodore 64"] = [1982, "Commodore International"]
    computercollection["TRS-80"] = [1977, "Tandy Corporation"]
    computercollection["Macintosh"] = [1984, "Apple Inc."]
    
    #b
    print(oldest_boy(computercollection))
    
    #c
    print(sorty_boy(computercollection))
    print(num_machines(computercollection))