#!/usr/bin/env python3

class Fridge:
    def __init__(self):
        self.storage = []

    def find(self, name):
        for i in self:
            if i[1] == name:
                return i
            return None

    def inventory(self):
        return self.storage

    def take(self, item):
        if item not in self.storage: 
            raise Warning("Item not in Fridge")
        else: self.storage.remove(item)
        return item

    def store(self, tup):
        self.storage.append(tup)

    def take_before(self, date):
        items = []
        for i in self.storage:
            if i[0] < date:
                self.storage.remove(i)
                items.append(i)
            else: continue

        return items

    def __len__(self):
        return len(self.storage)
    
    def __iter__(self):
        return iter(self.storage)



if __name__ == '__main__':
    f = Fridge()
    f.store((191112, "Butter"))
    f.store((191230, "Milk"))
    f.store((190530, "Chocolate"))
    print(f.find("Milk"))
    print(f.inventory())
    f.take((191112, "Butter"))
    print(f.inventory())