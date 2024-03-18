# models/Person.py

from typing import List
from models.DVD import DVD
from models.Livre import Livre

class Membre() :
    
    def __init__(self, nom: str, prenom: str, adress: str, email: str, documents_empruntes: List[DVD|Livre] = []) -> None :
        self.nom = nom
        self.prenom = prenom
        self.adress = adress
        self.email = email
        documents_empruntes = documents_empruntes

    def emprunter_document(self, document: DVD|Livre) -> None:
        if self.documents_empruntes.length() < 3:
            self.documents_empruntes.append(document)
            document.emprunter
            print(f"{self.nom} {self.prenom} a emprunté {document.title}")
        else:
            print(f"{self.nom} {self.prenom} ne peut pas emprunter plus de 3 documents à la fois.")
    
    def retourner_document(self, document: DVD|Livre) -> None:
        if document in self.documents_empruntes:
            self.documents_empruntes.remove(document)
            document.retourner
            print(f"{self.nom} {self.prenom} a retourné {document.title}")
        else:
            print(f"{self.nom} {self.prenom} n'a pas emprunté ce document.")
    
    def afficher_documents_empruntes(self) -> None:
        if self.documents_empruntes.length() > 0:
            print(f"Documents empruntés par {self.nom} {self.prenom}:")
            for document in self.documents_empruntes:
                print("{document.title} {document.author}, {document.release_date}")
        else:
            print(f"{self.nom} {self.prenom} n'a pas emprunté de document.")
    
    
    @nom.setter
    def nom(self, nom: str) -> None:
        self.nom = nom
    
    @nom.getter
    def nom(self) -> str:
        return self.nom
    
    @prenom.setter
    def prenom(self, prenom: str) -> None:
        self.prenom = prenom
    
    @prenom.getter
    def prenom(self) -> str:
        return self.prenom
    
    @adress.setter
    def adress(self, adress: str) -> None:
        self.adress = adress
    
    @adress.getter
    def adress(self) -> str:
        return self.adress
    
    @email.setter
    def email(self, email: str) -> None:
        self.email = email
    
    @email.getter
    def email(self) -> str:
        return self.email
    
    @documents_empruntes.setter
    def documents_empruntes(self, documents_empruntes: List[DVD|Livre]) -> None:
        self.documents_empruntes = documents_empruntes
    
    @documents_empruntes.getter
    def documents_empruntes(self) -> List[DVD|Livre]:
        return self.documents_empruntes