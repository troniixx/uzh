def fine_calculator(area,speed):

    #checks per area
    areacode = (("urban", 50, 1), ("expressway", 100, 0.8), ("motorway", 120, 0.5))
    if not isinstance(area, str): return "Invalid Area Type"
    for i in range(3):
        if area==areacode[i][0]:
            area =i
            break
    else: return "Invalid Area Value"

    #checks per speed
    if not isfloat(speed): return "Invalid Speed Type"
    speed=float(speed)
    if speed < 0: return "Invalid Speed Value"

    #calc
    if speed < areacode[area][1]: return 0
    return int((((speed/areacode[area][1]-1)*100)**2)*areacode[area][2])

print(fine_calculator("motorway", 180))