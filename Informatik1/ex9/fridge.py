#!/usr/bin/env python3
__author__ = "Mert Erol"
class Fridge:

    def __init__(self):
        self.__storage = []

    def __str__(self):
        fridge_info = "Fridge information: "
        fridge_info += "\nContents: " + str(self.__storage)
        return fridge_info
    
    def __iter__(self):
        self.fridge = 0
        return self

    def __len__(self): #check how many items are in the fridge
        return len(self.__storage)

    def __iter__(self):
        return iter(self.__storage)

    def __next__(self):
        return next(iter(self.__storage))

    def store(self, tup):
            self.__storage.append(tup)

    def find(self, name): #look up if item in fridge and best before
        sorted_storage = sorted(self.__storage)
        for item in sorted_storage:
            if item[1] == name:
                return "The item " + str(name) + " with the earliest eat-by date is in index " + str(self.__storage.index(item)) + "!"
            else:
                return None
        
        return sorted_storage

    def take_closest(self):
        x = sorted(self.__storage)
        del x[0]
        return x
    
    def take_before(self, date):
        new_list = []
        out = [item for item in self.__storage if item[0] == date]

        if len(out) == 0:
            return []
        else:
            for item in self.__storage:
                if item not in out:
                    new_list.append(item)

        return new_list

    def take(self, name): #remove item from fridge
        if name not in self.__storage:
            raise Warning('Item not in Fridge!')
        else:
            self.__storage.remove(name)

        return name

    


if __name__ == '__main__':
    f = Fridge()
    f.store((191112, "Butter"))
    print(f.__storage)
    f.take((191112, "Butter"))
    print(f.__storage)
