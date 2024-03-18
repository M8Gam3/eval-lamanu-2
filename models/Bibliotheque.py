# models/Person.py

from typing import List
from models.Document import Document

class Bibliotheque() :
    
    def __init__(self, documents) -> None :
        self.documents = documents
    
    def ajouter_document(self, document):
        self.documents.append(document)
    
    def supprimer_document(self,document):
        self.documents.remove(document)
    
    def rechercher_document():
        pass