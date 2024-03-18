# models/Person.py

from typing import List
from models.Membre import Membre
from models.DVD import DVD
from models.Livre import Livre
from models.Bibliotheque import Bibliotheque

class Employe() :
    
    def __init__(self, salaire: int, nom: str, prenom: str, adress: str, email: str, documents_empruntes: List[DVD|Livre] = []) -> None :
        super(Membre, self).__init__(nom, prenom, adress, email, documents_empruntes)
        salaire = salaire
    
    def ajouter_document(self, bibliotheque: Bibliotheque, document: DVD|Livre) -> None:
        bibliotheque.ajouter_document(document)
        print("{self.nom} {self.prenom} a ajouté le document {document.title} à la bibliothèque.")
    
    def supprimer_document(self, bibliotheque: Bibliotheque, document: DVD|Livre) -> None:
        bibliotheque.supprimer_document(document)
        print("{self.nom} {self.prenom} a supprimé le document {document.title} de la bibliothèque.")
    
    
    @salaire.setter
    def salaire(self, salaire: int) -> None:
        self.salaire = salaire
    
    @salaire.getter
    def salaire(self) -> int:
        return self.salaire