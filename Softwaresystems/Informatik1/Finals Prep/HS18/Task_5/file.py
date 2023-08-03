from FileSystemItem import FileSystemItem

class File(FileSystemItem):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size
