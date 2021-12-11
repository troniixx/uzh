class Item:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class Backpack:
    def __init__(self, max_volume):
        self.max_volume = max_volume
        self.storage = []

    def pack(self, item):
        if self.current_volume() + item.volume <= self.max_volume:
            raise Warning("Capacity exceeded")
        else: self.storage.append(item)

    def unpack(self):
        if self.storage:
            return self.storage.pop()
        else: return None

    def current_volume(self):
        cur = 0
        for item in self.storage:
            cur += item.volume
        return cur