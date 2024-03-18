import abc
from typing import List

# Abstract class
class Document(abc.ABC):
    
    def __init__(self, title: str, author: str, release_date: str, is_book: bool = False) -> None :
        self.title = title
        self.author = author
        self.release_date = release_date
        self.is_book = is_book
    
    @abc.abstractmethod
    def emprunter(self) -> None:
        pass
    
    @abc.abstractmethod
    def retourner(self) -> None:
        pass
    
    
    @title.setter
    def title(self, title: str) -> None:
        self.title = title
    
    @title.getter
    def title(self) -> str:
        return self.title
    
    @author.setter
    def author(self, author: str) -> None:
        self.author = author
    
    @author.getter
    def author(self) -> str:
        return self.author
    
    @release_date.setter
    def release_date(self, release_date: str) -> None:
        self.release_date = release_date
    
    @release_date.getter
    def release_date(self) -> str:
        return self.release_date
    
    @is_book.setter
    def is_book(self, is_book: bool) -> None:
        self.is_book = is_book
    
    @is_book.getter
    def is_book(self) -> bool:
        return self.is_book
