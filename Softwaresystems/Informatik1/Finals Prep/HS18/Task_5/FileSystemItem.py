from abc import ABC
from abc import abstractmethod

class FileSystemItem(ABC):
    
    @abstractmethod
    def size(self):
        pass

