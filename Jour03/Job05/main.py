import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))

    def lancerJeu(self):
        self.choisirNiveau()

        if self.niveau == 1:
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 50)
        elif self.niveau == 2:
            joueur = Personnage("Joueur", 80)
            ennemi = Personnage("Ennemi", 70)
        elif self.niveau == 3:
            joueur = Personnage("Joueur", 60)
            ennemi = Personnage("Ennemi", 90)
        else:
            print("Niveau non valide. Le jeu se lance au niveau 1 par défaut.")
            joueur = Personnage("Joueur", 100)
            ennemi = Personnage("Ennemi", 50)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu ! {joueur.nom} remporte la victoire.")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu ! {ennemi.nom} remporte la victoire.")
                break

            print(f"{joueur.nom} - Vie: {joueur.vie} | {ennemi.nom} - Vie: {ennemi.vie}")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()
