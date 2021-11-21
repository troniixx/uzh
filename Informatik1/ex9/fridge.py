#!/usr/bin/env python3
__author__ = "Mert Erol"
class Fridge:

    def __init__(self):
        self.storage = []
        self.max = len(self.storage)

    def __str__(self):
            fridge_info = "Fridge information: "
            fridge_info += "\nContents: " + str(self.storage)
            return fridge_info

    def __next__(self):
        pass
    
    def __iter__(self):
        self.fridge = 0
        return self

    def __len__(self): #check how many items are in the fridge
        return len(self.storage)

    def __iter__(self):
        return iter(self.storage)

    def __next__(self):
        return next(iter(self.storage))

    def store(self, tup):
            self.storage.append(tup)

    def find(self, name): #look up if item in fridge and best before
        sorted_storage = sorted(self.storage)
        for item in sorted_storage:
            if item[1] == name:
                return "The item " + str(name) + " with the earliest eat-by date is in index " + str(self.storage.index(item)) + "!"
            else:
                return None
        
        return sorted_storage

    def take_closest(self):
        x = sorted(self.storage)
        del x[0]
        return x
    
    def take_before(self, date):
        new_list = []
        out = [item for item in self.storage if item[0] == date]

        if len(out) == 0:
            return []
        else:
            for item in self.storage:
                if item not in out:
                    new_list.append(item)

        return new_list

    def take(self, name): #remove item from fridge
        if name not in self.storage:
            raise Warning('Item not in Fridge!')
        else:
            self.storage.remove(name)

        return name

    


if __name__ == '__main__':
    f = Fridge()
    f.store((191112, "Butter"))
    print(f.storage)
    f.take((191112, "Butter"))
    print(f.storage)
