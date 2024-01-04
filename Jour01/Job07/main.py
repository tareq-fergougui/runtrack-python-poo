class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation de la classe Personnage
mon_personnage = Personnage()

# Affichage de la position initiale
print("Position initiale :", mon_personnage.position())

# Déplacement du personnage vers la droite et vers le bas
mon_personnage.droite()
mon_personnage.bas()

# Affichage de la nouvelle position
print("Nouvelle position :", mon_personnage.position())
