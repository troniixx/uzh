#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def stats(students):
    student = {}
    whole = {}

    for k, v in students.items():
        total = 0
        for subject, grade in v:
            total += grade
        student[k] = round(total/len(v), 2)
    
    for k, v in students.items():
        for subject, grade in v:
            if subject not in whole:
                whole[subject] = []
            whole[subject].append(grade)

    for k, v in whole.items():
        whole[k] = round(sum(v) / len(v), 2)

    
    return student, whole



#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
raw = {"12-345-678": [("Math", 5.5),  ("Biology", 5.75), ("Latin", 4.25)],
    "09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
    "01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
    }
students, subjects = stats(raw)
assert(len(students) == 3)
assert(len(subjects) == 4)
assert(students["12-345-678"] == 5.17)
assert(subjects["Latin"] == 4.08)