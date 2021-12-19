class Employee:
    id = 0
    def __init__(self, name):
        self.name = name
        self.id = Employee.id
        Employee.id += 1
emp = Employee("Marc")
print(emp.id)