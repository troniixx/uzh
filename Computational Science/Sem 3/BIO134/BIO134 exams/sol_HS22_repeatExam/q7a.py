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


for individual in persons:
    # extract dates
    birth_day, birth_month, birth_year = persons[individual][1].split()
    death_day, death_month, death_year = persons[individual][2].split()
    
    # calculates simpole calendar years. includes the entire birth year and excludes the last year of live. 
    # correct age in years only if person died later in the year than was born
    years_notcorrected_indays = (int(death_year)-int(birth_year)) * 365    
    
    
    # as always: there are many different strategies to find correct age!
    
    # find the number of the months
    for i in range(len(months)):
        if months[i][0] == birth_month:
            birth_month_no = i
        if months[i][0] == death_month:
            death_month_no = i
                
    # find the number of days that the person was not alive yet in its first year
    # these need to be subtracted from the calculated years
    firstyear_days_notbornyet = int(birth_day) # days from the birthmonth
    for i in range(1, int(birth_month_no)):
        firstyear_days_notbornyet += months[i][1]
    
    # find the number of days that the person was still alive in its last year
    # these need to be added to the calculated years
    lastyear_days_alive = int(death_day)
    for i in range(1, int(death_month_no)):
        lastyear_days_alive += months[i][1]
    
    days_alive = years_notcorrected_indays - firstyear_days_notbornyet + lastyear_days_alive 
    years = int(days_alive/365)
    days_remaining = days_alive % 365
    persons[individual].append(years)
    persons[individual].append(days_remaining)
    
print()
print(persons)



