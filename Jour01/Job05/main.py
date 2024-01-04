class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée x : {self.x}")

    def afficherY(self):
        print(f"Coordonnée y : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

# Exemple d'utilisation de la classe Point
point1 = Point(3, 4)

# Affichage des coordonnées initiales
point1.afficherLesPoints()

# Affichage de x et y
point1.afficherX()
point1.afficherY()

# Changement des valeurs de x et y
point1.changerX(7)
point1.changerY(9)

# Affichage des nouvelles coordonnées
point1.afficherLesPoints()
