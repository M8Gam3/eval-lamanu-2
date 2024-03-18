# models/Person.py

from typing import List
from models.Document import Document

class DVD(Document) :
    
    def __init__(self, duration, title, release_date, is_book) -> None :
        super(Document, self).__init__(title, release_date, is_book)
        self.duration = duration
    
    def emprunter(self):
        print(f"Le DVD {self.title} a été emprunté.")
        self.is_book = True
    
    def retourner(self):
        print(f"Le DVD {self.title} a été rendu.")
        self.is_book = False