from abc import ABC, abstractmethod

class Command(ABC):
    
    line = None

    def __init__(self, line):

        self.line = line


    @abstractmethod
    def run(self) -> bool:

        return True
    
    @abstractmethod
    def get_data(self):
        
        return None