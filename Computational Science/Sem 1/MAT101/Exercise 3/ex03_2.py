#Exercise 2a
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

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
    days_start = days_since_new_year(start)
    days_end = days_since_new_year(end)
    
    if start[2] == end[2]:
        return days_end - days_start
    else:
        total_days = days_end + (366 if is_leap_year(end[2]) else 365) - days_start
        for year in range(start[2] + 1, end[2]):
            total_days += 366 if is_leap_year(year) else 365
        return total_days
        
        
if __name__ == '__main__':
    print(is_leap_year(2000))
    print(days_since_new_year([1, 1]))
    print(days_since_new_year([19, 2]))
    print(days_between([1, 1, 2000], [1, 1, 2001]))
    print(days_between([1, 1, 2000], [1, 1, 2000]))
    print(days_between([25, 12, 2023], [4, 1, 2024]))