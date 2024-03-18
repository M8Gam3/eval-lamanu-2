# models/Person.py

from typing import List
from models.Document import Document

class Livre(Document) :
    
    def __init__(self, pages: int, title: str, author: str, release_date: str, is_book: bool = False) -> None :
        super(Document, self).__init__(title, author, release_date, is_book)
        self.pages = pages

    def emprunter(self) -> None:
        print(f"Le livre {self.title} a été emprunté.")
        self.is_book = True
    
    def retourner(self) -> None:
        print(f"Le livre {self.title} a été rendu.")
        self.is_book = False
    
    
    @pages.setter
    def pages(self, pages: int) -> None:
        self.pages = pages
    
    @pages.getter
    def pages(self) -> int:
        return self.pages