import FileSystemItem
from file import File

class Folder(FileSystemItem):
    def __init__(self, children):
        self.__children = []
    
    def get_size(self):
        sum = 0
        for file in self.__children:
            sum += file.size()
        return sum
