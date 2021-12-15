def stats(students):
    avg_student = {}
    avg_all = {}

    for k, v in students.items():
        tot = 0
        for subject, grade in v:
            tot += grade
        avg_student[k] = round(tot/len(v), 2)

    for k, v in students.items():
        for subject, grade in v:
            if subject not in avg_all:
                avg_all[subject] = []
            avg_all[subject].append(grade)

    for k, v in avg_all.items():
        avg_all[k] = round(sum(v) / len(v), 2)
    

    return avg_student, avg_all



# DO NOT SUBMIT THE LINES BELOW!
raw = {"12-345-678": [("Math", 5.5),  ("Biology", 5.75), ("Latin", 4.25)],
	"09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
	"01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
	}
students, subjects = stats(raw)
assert(len(students) == 3)
assert(len(subjects) == 4)
assert(students["12-345-678"] == 5.17)
assert(subjects["Latin"] == 4.08)