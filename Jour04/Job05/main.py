import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, rayon):
        self.radius = rayon
    
    def aire(self):
        return math.pi * self.radius**2

# Création d'une instance de Rectangle avec une largeur de 5 et une hauteur de 3
rectangle = Rectangle(5, 3)

# Affichage du résultat de la méthode aire de la classe Rectangle
print("Aire du rectangle :", rectangle.aire())

# Création d'une instance de Cercle avec un rayon de 2
cercle = Cercle(2)

# Affichage du résultat de la méthode aire de la classe Cercle
print("Aire du cercle :", cercle.aire())