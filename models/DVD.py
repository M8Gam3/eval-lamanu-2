# models/Person.py

from typing import List
from models.Document import Document

class DVD(Document) :
    
    def __init__(self, duration: int, title: str, author: str, release_date: str, is_book: bool = False) -> None :
        super(Document, self).__init__(title, author, release_date, is_book)
        self.duration = duration
    
    def emprunter(self) -> None:
        print(f"Le DVD {self.title} a été emprunté.")
        self.is_book = True
    
    def retourner(self) -> None:
        print(f"Le DVD {self.title} a été rendu.")
        self.is_book = False
    
    
    @duration.setter
    def duration(self, duration: int) -> None:
        self.duration = duration
    
    @duration.getter
    def duration(self) -> int:
        return self.duration