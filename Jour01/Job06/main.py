class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficherAge(self):
        print(f"Âge de l'animal : {self.age}")

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

    def afficherNom(self):
        print(f"Nom de l'animal : {self.prenom}")

# Instanciation d'un objet Animal
mon_animal = Animal()

# Affichage de l'âge initial
mon_animal.afficherAge()

# Vieillissement de l'animal
mon_animal.vieillir()

# Affichage du nouvel âge
mon_animal.afficherAge()

# Nommer l'animal
mon_animal.nommer("Luna")

# Affichage du nom de l'animal
mon_animal.afficherNom()
