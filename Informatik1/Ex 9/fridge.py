#!/usr/bin/env python3
__author__ = "Mert Erol"
class Fridge:

    def __init__(self):
        self.__storage = []

    def store(self, tup):
                self.__storage.append(tup)

    def inventory(self):
        return self.__storage

    def __str__(self):
        fridge_info = "Fridge information: "
        fridge_info += "\nContents: " + str(self.__storage)
        return fridge_info

    def __len__(self): #check how many items are in the fridge
        return len(self.__storage)

    def __iter__(self):
        return iter(sorted(self.__storage))

    #def __next__(self):
    #    return next(iter(self.__storage))

    def find(self, name): #look up if item in fridge and best before
        for i in self:
            if i[1] == name:
                return i
            return None
    
    def take_before(self, date):
        items = []
        for i in self.__storage:
            if i[0] < date:
                self.__storage.remove(i)
                items.append(i)
        return items

    def take(self, item): #remove item from fridge
        if item not in self.__storage:
            raise Warning('Item not in Fridge!')
        self.__storage.remove(item)
        return item
    


if __name__ == '__main__':
    f = Fridge()
    #f.store((191112, "Butter"))
    #print(f.inventory())
    #f.take((191112, "Butter"))
    #print(f.inventory())
