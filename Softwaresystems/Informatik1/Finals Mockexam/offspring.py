import random

class Person:
    def __init__(self, name = None, sex = None):
        self.name = name
        self.sex = random.choice(["m", "f"]) if sex is None else sex
        self.offspring = []

    def mate_with(self, other):
        if self.sex == other.sex:
            raise ValueError 
        child = Person()
        self.offspring.append(child)
        other.offspring.append(child)
        return child
    
    def __str__(self):
        if self.offspring:
            child = "child" if len(self.offspring) == 1 else "children"
            offspring = ", ".join([c.name for c in self.offspring])

            return  f"{self.name} ({self.sex}) has {len(self.offspring)} {child}: {offspring}"

        else: return f"{self.name} ({self.sex}) has no children"

    def __repr__(self):
        return self.__str__()


# DO NOT SUBMIT THE LINES BELOW!
p1 = Person("Mark", "m")
p2 = Person("Betty", "f")
p3 = Person("John", "m")
p4 = Person("Anna", "f")
child = p1.mate_with(p2)
assert(child.name == None)
child.name = "Andrea"
assert(len(p1.offspring) == 1)
child = p3.mate_with(p2)
assert(len(p2.offspring) == 2)
child.name = "Terry"
assert(p1.__str__() == "Mark (m) has 1 child: Andrea")
assert(p2.__str__() == "Betty (f) has 2 children: Andrea, Terry")
assert(p3.__repr__() == "John (m) has 1 child: Terry")
assert(p4.__repr__() == "Anna (f) has no children")