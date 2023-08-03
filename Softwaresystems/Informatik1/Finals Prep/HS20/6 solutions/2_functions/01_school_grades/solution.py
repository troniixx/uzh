#!/usr/bin/env python3

def stats(students):
    avg_per_student = {}
    for k, v in students.items():
        total = 0
        for subject, grade in v:
            total += grade
        avg_per_student[k] = round(total/len(v), 2)
    avg_per_subject = {}
    for k, v in students.items():
        for subject, grade in v:
            if subject not in avg_per_subject:
                avg_per_subject[subject] = []
            avg_per_subject[subject].append(grade)
    for k, v in avg_per_subject.items():
        avg_per_subject[k] = round(sum(v) / len(v), 2)
    return avg_per_student, avg_per_subject

