# s = scored points

def grade(s):
    if s > 100 or s < 0:
        grade = "Invalid s"
    elif s > 90 and s <= 100:
        grade = 6.0
    elif s > 80 and s <= 90:
        grade = 5.5
    elif s > 70 and s <= 80:
        grade = 5.0
    elif s > 60 and s <= 70:
        grade = 4.5
    elif s > 50 and s <= 60:
        grade = 4.0
    else:
        grade = "Fail"
    
    return grade

if __name__ == "__main__":
    print(grade(101))
    print(grade(100))
    print(grade(95))    
    print(grade(90))
    print(grade(80))
    print(grade(70))
    print(grade(60))
    print(grade(50))
    print(grade(0))