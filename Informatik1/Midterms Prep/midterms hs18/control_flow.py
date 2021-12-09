def get_age_desc(age):
    if age <= 0:
        return "invalid"

    if age < 3:
        return "Toddler"
    if age >= 3 and age < 18:
        return "Child"
    if age >= 18 and age < 65:
        return "Adult"
    else:
        return "Senior"

print(get_age_desc(0))
print(get_age_desc(1))
print(get_age_desc(3))
print(get_age_desc(14))
print(get_age_desc(18))
print(get_age_desc(65))
