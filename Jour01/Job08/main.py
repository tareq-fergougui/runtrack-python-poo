import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Informations du cercle - Rayon : {self.rayon}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

# Création de deux cercles avec des rayons 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations pour chaque cercle
cercle1.afficherInfos()
cercle2.afficherInfos()

# Affichage de la circonférence pour chaque cercle
print("Circonférence du cercle 1 :", cercle1.circonference())
print("Circonférence du cercle 2 :", cercle2.circonference())

# Affichage du diamètre pour chaque cercle
print("Diamètre du cercle 1 :", cercle1.diametre())
print("Diamètre du cercle 2 :", cercle2.diametre())

# Affichage de l'aire pour chaque cercle
print("Aire du cercle 1 :", cercle1.aire())
print("Aire du cercle 2 :", cercle2.aire())
