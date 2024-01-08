class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")

class Professeur(Personne):
    def enseigner(self):
        print("Le cours commence.")

# Création de l'objet Eleve
eleve = Eleve(nom="Pierre", age=15)

# Utilisation des méthodes pour l'élève
eleve.bonjour()
eleve.allerEnCours()

# Redéfinition de l'âge de l'élève à 15 ans
eleve.age = 15

# Création de l'objet Professeur
professeur = Professeur(nom="Prof. Smith", age=40)

# Utilisation des méthodes pour le professeur
professeur.bonjour()
professeur.enseigner()
