#!/usr/bin/env python3

import random

class Person:
    def __init__(self, name=None, sex=None):
        self.sex = random.choice(["m", "f"]) if sex is None else sex
        self.name = name
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
            return f"{self.name} ({self.sex}) has {len(self.offspring)} {child}: {offspring}"
        return f"{self.name} ({self.sex}) has no children"

    def __repr__(self):
        return self.__str__()

