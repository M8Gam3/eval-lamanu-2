# models/Person.py

from typing import List
from models.Membre import Membre
from models.DVD import DVD
from models.Livre import Livre
from models.Bibliotheque import Bibliotheque

class Etudiant() :
    
    def __init__(self, numero_etudiant: int, nom: str, prenom: str, adress: str, email: str, documents_empruntes: List[DVD|Livre] = []) -> None :
        super(Membre, self).__init__(nom, prenom, adress, email, documents_empruntes)
        numero_etudiant = numero_etudiant
    
    def emprunter_document(self, document: DVD|Livre, bibliotheque: Bibliotheque) -> None:
        if document in bibliotheque.documents:
            print(f"{self.nom} {self.prenom} ne peut pas emprunter un livre qui n'est pas dans la bibliotheque.")
        elif self.documents_empruntes.length() < 5:
            self.documents_empruntes.append(document)
            document.emprunter
            print(f"{self.nom} {self.prenom} a emprunté {document.title}")
        else:
            print(f"{self.nom} {self.prenom} ne peut pas emprunter plus de 5 documents à la fois.")
    
    
    @numero_etudiant.setter
    def numero_etudiant(self, numero_etudiant: int) -> None:
        self.numero_etudiant = numero_etudiant
    
    @numero_etudiant.getter
    def numero_etudiant(self) -> int:
        return self.numero_etudiant