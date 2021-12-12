#!/usr/bin/env python3

class Classroom:
    def __init__(self):
        self.students = {}

    def add(self, student):
        if student.matno in self.students:
            raise ValueError
        self.students[student.matno] = student

    def remove(self, matno):
        if matno not in self.students:
            raise IndexError
        del self.students[matno]

class Student:
    matno = 0
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.matno = Student.matno
        Student.matno += 1

