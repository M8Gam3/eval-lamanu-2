from models.DVD import DVD
from models.Livre import Livre
from models.Bibliotheque import Bibliotheque
from models.Membre import Membre
from models.Etudiant import Etudiant
from models.Employe import Employe

class_list = {
    "dvd": DVD,
    "livre": Livre,
    "bibliotheque": Bibliotheque,
    "membre": Membre,
    "etudiant": Etudiant,
    "employe": Employe,
}

documents = [
    class_list['livre'](653, 'Eragon', 'Christopher Paolini', '26/08/2003'),
    class_list['dvd'](105, 'Indiana Jones : les aventuriers de l\'arche perdue', 'Steven Spielberg', '16/09/1981'), 
    class_list['dvd'](127, 'Jurassic Park', 'Steven Spielberg', '20/10/1993'), 
]

users = []

bibliotheque = class_list['bibliotheque']

for document in documents:
    bibliotheque.ajouter_document(document)

bibliotheque.afficher_documents()

bibliotheque.rechercher_document('Steven Spielberg')

bibliotheque.supprimer_document(documents[1])

users[0] = class_list['employe'](1480.75, 'Dupont', 'Jean', '12 Rue des Lilas 75020 Paris', 'jean.dupont@gmail.com')

bibliotheque.ajouter_document(documents[1])

bibliotheque.supprimer_document(documents[2])

users[1] = class_list['etudiant'](3096874, 'Marie', 'Dubois', '10 Rue de la Paix 69002 Lyon', 'marie.dubois@gmail.com')

users[1].emprunter_document(documents[0])
users[1].emprunter_document(documents[2])