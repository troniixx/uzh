#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question 7

persons = {}
persons['darwin'] = ['Charles Darwin','12 February 1809', '19 April 1882'] 
persons['shakespeare'] = ['William Shakespeare', '26 April 1564','23 April 1616'] 
persons['cervantes'] = ['Miguel de Cervantes', '29 September 1547','23 April 1616']
persons['lincoln'] = ['Abraham Lincoln', '12 February 1809','15 April 1865']

months = [['January', 31], ['February', 28], ['March', 31], ['April', 30], \
['May', 31], ['June', 30], ['July', 31], ['August', 31], ['September', 30], \
['October', 31], ['November', 30], ['December', 31]]

    
def daysSinceChrist(day, month, year):

    result = int(year) * 365
    for entry in months:
        if entry[0] == month: break
        result += entry[1]
    result += int(day)

    return result

# main execution:

for entry in persons:

    (birthday, birthmonth, birthyear) = persons[entry][1].split()
    (deathday, deathmonth, deathyear) = persons[entry][2].split()

    ageInDays = daysSinceChrist(deathday, deathmonth, deathyear)
    ageInDays -= daysSinceChrist(birthday, birthmonth, birthyear)

    ageInYears = ageInDays // 365
    ageRemainder = ageInDays % 365

    persons[entry].append(ageInYears)
    persons[entry].append(ageRemainder)

print(persons)
