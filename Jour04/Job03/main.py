class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur


# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 3)

# Accès aux attributs avec les assesseurs
print("Longueur du rectangle :", rectangle.get_longueur())
print("Largeur du rectangle :", rectangle.get_largeur())

# Modification des attributs avec les mutateurs
rectangle.set_longueur(7)
rectangle.set_largeur(4)

# Affichage du périmètre et de la surface du rectangle
print("Périmètre du rectangle :", rectangle.perimetre())
print("Surface du rectangle :", rectangle.surface())

# Instanciation de la classe Parallelepipede
parallelepiped = Parallelepipede(5, 3, 2)

# Accès aux attributs avec les assesseurs
print("Longueur du parallélépipède :", parallelepiped.get_longueur())
print("Largeur du parallélépipède :", parallelepiped.get_largeur())
print("Hauteur du parallélépipède :", parallelepiped.get_hauteur())

# Modification des attributs avec les mutateurs
parallelepiped.set_longueur(7)
parallelepiped.set_largeur(4)
parallelepiped.set_hauteur(6)

# Affichage du périmètre, de la surface et du volume du parallélépipède
print("Périmètre du parallélépipède :", parallelepiped.perimetre())
print("Surface du parallélépipède :", parallelepiped.surface())
print("Volume du parallélépipède :", parallelepiped.volume())