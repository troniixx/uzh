#!/usr/bin/env python3

# This solution adheres to the task description including a name parameter.
# Because the assertions for the Event constructor are faulty in the task,
# omitting the name parameter and get_name method is also an accepted solution.
class Event:
    def __init__(self, name, seats):
        self.__name = name
        self.__seats = [None] * seats

    def get_name(self):
        return self.__name

    def enter(self, seat_no, name):
        if seat_no < 1 or seat_no > len(self.__seats):
            raise IndexError
        if self.__seats[seat_no-1]:
            raise NameError
        self.__seats[seat_no-1] = name

    def get(self, seat_no):
        if seat_no < 1 or seat_no > len(self.__seats):
            raise IndexError
        return self.__seats[seat_no-1]

    def occupied(self):
        return sum(1 for s in self.__seats if s)

    def empty(self):
        return len(self.__seats) - self.occupied()

    def __lt__(self, other):
        return self.occupied() < other.occupied()

    def __gt__(self, other):
        return self.occupied() > other.occupied()

    def __eq__(self, other):
        return self.occupied() == other.occupied()