class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def en_marche(self):
        return self.__en_marche

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("La voiture ne peut pas démarrer car le réservoir est presque vide.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

    def __verifier_plein(self):
        return self.__reservoir

# Création d'un objet représentant une voiture
ma_voiture = Voiture("Renault", "Clio", 2020, 50000)

# Utilisation des mutateurs pour modifier les attributs de la voiture
ma_voiture.set_marque("Peugeot")
ma_voiture.set_modele("208")
ma_voiture.set_annee(2022)
ma_voiture.set_kilometrage(10000)

# Utilisation des accesseurs pour obtenir les attributs de la voiture
print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()