import abc
from typing import List

# Abstract class
class Document(abc.ABC):
    
    def __init__(self, title, release_date, is_book = False) -> None :
        self.title = title
        self.release_date = release_date
        self.is_book = is_book
    
    @abc.abstractmethod
    def emprunter(self):
        pass
    
    @abc.abstractmethod
    def retourner(self):
        pass
