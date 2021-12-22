#WORKS POG
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

class Researcher(Employee): #festangestellt, fixe lohn
    ide = 0
    def __init__(self,name, lohn):
        self.name = name
        self.lohn = lohn
        self.ide = Researcher.ide
        Researcher.ide += 1 

    def get_monthly_salary(self):
        return self.lohn/12

    def get_name(self):
        return self.name

    def get_id(self):
        return self.ide

    def __str__(self):
        return f"Salary: {self.get_monatslohn()} ({self.ide})"
class Lecturer(Employee):
    #studenbasis bezahlt,  studenlohn und fixe anzahl stunden, mindestlohn
    def __init__(self, name, hours, studenlohn):
        self.name = name
        self.hours = hours
        self.studenlohn = studenlohn

    def get_monthly_salary(self):
        return self.studenlohn*self.hours

    def __str__(self):
        return f"Salary: {self.get_monatslohn()} (temp)"

    def get_name(self):
        return self.name

class University(ABC):
    def __init__(self,name):
        self.name = name
        self.employees = []
    
    def get_name(self):
        return self.name

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_monthly_staff_cost(self):
        cost = 0
        for employee in self.employees:
            cost += employee.get_monthly_salary()
        return cost


# DO NOT SUBMIT THE LINES BELOW!
e = University("Lamebridge")
i1 = Researcher("Bob", 60000) # yearly salary
i2 = Researcher("Alice", 75000) # yearly salary
i3 = Lecturer("Taylor", 21.50, 15) # hourly salary, hours per month
assert i1.get_name() == "Bob"
assert i3.get_name() == "Taylor"
assert i1.get_id() == 0
assert i2.get_id() == 1
assert i1.get_monthly_salary() > 4000
assert i3.get_monthly_salary() == 322.50
e.add_employee(i1)
e.add_employee(i2)
e.add_employee(i3)
assert e.get_monthly_staff_cost() > 9000