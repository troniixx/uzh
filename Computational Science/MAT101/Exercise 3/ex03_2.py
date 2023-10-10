#Exercise 2a
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
        return True
    return False

#Exercise 2b
def days_since_new_year(date):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31]
    day = date[0]
    month = date[1]
    result = day
    
    for day in range(1, month):
        result += months[day]
        
    return result-1

#Exercise 2c
def days_between(start, end):
    months = []
    day_start = start[0], month_start = start[1], year_start = start[2]
    
    day_end = end[0], month_end = end[1], year_end = end[2]
    
    if year_start == year_end:
        if month_start == month_end:
            return day_end - day_start
        else:
            pass