class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

# Création d'un rectangle avec les valeurs initiales
mon_rectangle = Rectangle(10, 5)

# Affichage des valeurs initiales
print("Longueur :", mon_rectangle.get_longueur())
print("Largeur :", mon_rectangle.get_largeur())

# Modification des valeurs
mon_rectangle.set_longueur(8)
mon_rectangle.set_largeur(3)

# Affichage des nouvelles valeurs
print("Nouvelle longueur :", mon_rectangle.get_longueur())
print("Nouvelle largeur :", mon_rectangle.get_largeur())