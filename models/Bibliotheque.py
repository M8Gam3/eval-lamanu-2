# models/Person.py

from typing import List
from models.Document import Document
from models.DVD import DVD
from models.Livre import Livre

class Bibliotheque() :
    
    def __init__(self, documents: List[int] = []) -> None:
        self.documents = documents
    
    def ajouter_document(self, document: DVD|Livre) -> None:
        self.documents.append(document)
    
    def supprimer_document(self, document: DVD|Livre) -> None:
        self.documents.remove(document)
    
    def rechercher_document(self, search: str) -> None:
        document_filter = []
        for document in self.documents:
            if document.author == search:
                document_filter.append(document)
        if document_filter == []:
            print('Aucun document trouvé avec cet auteur.')
        else:
            for document in document_filter:
                print(f"{document.title} {document.author},{document.release_date}")
    
    def afficher_documents(self) -> None:
        for document in self.documents:
            print(f"{document.title} {document.author},{document.release_date}")
    
    
    @documents.setter
    def documents(self, documents: List[int] = []) -> None:
        self.documents = documents
    
    @documents.getter
    def documents(self) -> List[int]:
        return self.documents