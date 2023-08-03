#WORKS POG
class Event:
    def __init__(self, space, name = None):
        self.name = name
        self.__space = space
        self.__occ = {}

    def enter(self, name, seat):
        if seat  in self.__occ:
            raise NameError
        else: self.__occ[name] = seat

    def get(self, seat):
        if seat < 1 or seat > self.__space:
            raise IndexError
        
        if seat not in self.__occ:
            return None
        else: return self.__occ[seat]

    def occupied(self):
        return len(self.__occ)

    def empty(self):
        return self.__space - len(self.__occ)

    def get_name(self):
        return self.name

    def __lt__(self, other):
        return len(self.__occ) < len(other.__occ)

    def __gt__(self, other):
        return len(self.__occ) > len(other.__occ)

    def __eq__(self, other):
        return len(self.__occ) == len(other.__occ)

# DO NOT SUBMIT THE LINES BELOW!
e1 = Event(150)
e1.enter(45, "Alice")
assert e1.get(45) == "Alice"
e1.enter(42, "Bob")
assert e1.occupied() == 2
assert e1.empty() == 148
e2 = Event(40)
assert e2.get(40) == None
e2.enter(1, "Andrea")
e2.enter(2, "Beatrice")
assert e2 == e1
e2.enter(20, "Charly")
assert e2 > e1