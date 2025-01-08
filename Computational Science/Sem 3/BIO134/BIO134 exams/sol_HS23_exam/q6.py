#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 6

students = [['11-287-233', 'Justus', 'Meier', 'Justus', 'C'], 
            ['08-609-029', 'Luna Meier', 'Meier', 'Luna', 'A'], 
            ['11-237-784', 'Mhood', 'Hood', 'Maria', 'C'], 
            ['08-169-553', 'Shea_Toby', 'Shea', 'Toby', 'B'], 
            ['08-364-725', 'linC', 'Lin-Schmidt', 'Cason', 'B'], 
            ['08-959-799', 'perez123', 'Perez Sanchez', 'Maria', 'B'], 
            ['09-106-042', 'shayrom', 'Romero', 'Shayna', 'A']]

results = [['Justus',12,13,5], ['Luna Meier',10,11,14], ['Shea_Toby',7,6,2], 
['Mhood',8,10,3], ['linC',13,10,15], ['perez123',2,3,0], ['shayrom',5,8,4]]

# create a dictionary with keys=usernames, values=total scores
# find the best total scores and corresponding username
totScorePerUsername = {}
bestScore = 0
bestUsername = ''
for user in results:
    totScore = sum(user[1:]) # keep general to allow more scores
    if totScore > bestScore:
        bestScore = totScore
        bestUsername = user[0] # remember the corresponding username to best points
    totScorePerUsername[user[0]] = totScore

# create a dictionary with keys=groups and values=collection of students
# keep all necessary info from students list plus add the scores for each student
studentsPerGroup = {}
for student in students:
    matr, user, last, first, group = student
    totScore = totScorePerUsername[user] # match the students and scores via username NOT index!
    if user == bestUsername:
        bestStudent = [matr, last, first, user, group]
        
    if not group in studentsPerGroup:
        studentsPerGroup[group] = []
    studentsPerGroup[group].append([totScore, matr, last, first])
    studentsPerGroup[group].sort() # sort the students by total scores

# calculate average score per group
groupAverages = {}
for group in studentsPerGroup:
    groupAverages[group] = 0
    for student in studentsPerGroup[group]:
        totScore = student[0]
        groupAverages[group] += totScore
    groupAverages[group] = groupAverages[group]/len(studentsPerGroup[group])

# print what is required
print('a)')
print('best student: {} points'.format(bestScore))
print(' '.join(bestStudent))
print('b)')
for group in sorted(studentsPerGroup.keys()): # sort the groups
    print('group', group)
    for student in studentsPerGroup[group]:
        print(student[0], ' '.join(student[1:])) # ''.join(student) fails as student[0] is int
    print('group average:', groupAverages[group])
    


