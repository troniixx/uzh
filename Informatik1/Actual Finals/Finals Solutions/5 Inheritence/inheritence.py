#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def get_monthly_salary(self):
        pass

class Researcher(Employee):
    seq = 0
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.__annual_salary = annual_salary
        self.__id = Researcher.seq
        Researcher.seq += 1

    def get_id(self):
        return self.__id

    def get_monthly_salary(self):
        return self.__annual_salary / 12

    def __str__(self):
        return f"{self.get_name()}: {self.get_monthly_salary()} ({self.__id})"

class Lecturer(Employee):
    def __init__(self, name, hourly_salary, hours_per_month):
        super().__init__(name)
        if hourly_salary < 9.4:
            raise Warning
        self.__hourly_salary = hourly_salary
        self.__hours_per_month = hours_per_month

    def get_monthly_salary(self):
        return self.__hourly_salary * self.__hours_per_month

    def __str__(self):
        return f"{self.get_name()}: {self.get_monthly_salary()} (temp)"

class University:
    def __init__(self, name):
        self.name = name
        self.__employees = []

    def add_employee(self, employee):
        if employee in self.__employees:
            raise Warning
        self.__employees.append(employee)

    def get_monthly_staff_cost(self):
        res = 0
        for e in self.__employees:
            res += e.get_monthly_salary()
        return res