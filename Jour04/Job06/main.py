class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Année :", self.annee)
        print("Prix :", self.prix)

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)

    def demarrer(self):
        print("La voiture démarre")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roue)

    def demarrer(self):
        print("La moto démarre")

# Instanciation d'un objet "Voiture"
voiture = Voiture("Renault", "Clio", 2018, 12000)
voiture.informationsVehicule()
voiture.demarrer()

print()

# Instanciation d'un objet "Moto"
moto = Moto("Yamaha", "MT-07", 2020, 8000)
moto.informationsVehicule()
moto.demarrer()