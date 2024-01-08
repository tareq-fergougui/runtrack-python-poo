import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    def get_valeur(self):
        return self.valeur


class Jeu:
    def __init__(self):
        self.paquet = []
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self):
        return self.paquet.pop()

    def evaluer_main(self, main):
        total = 0
        as_count = 0

        for carte in main:
            valeur = carte.get_valeur()
            if valeur.isdigit():
                total += int(valeur)
            elif valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif valeur == 'As':
                total += 11
                as_count += 1

        while total > 21 and as_count > 0:
            total -= 10
            as_count -= 1

        return total


# Exemple d'utilisation
jeu = Jeu()
jeu.melanger()

main_joueur = []
main_croupier = []

main_joueur.append(jeu.distribuer_cartes())
main_croupier.append(jeu.distribuer_cartes())
main_joueur.append(jeu.distribuer_cartes())
main_croupier.append(jeu.distribuer_cartes())

print("Main du joueur:")
for carte in main_joueur:
    print(carte)

print("\nMain du croupier:")
print(main_croupier[0])  # Ne montrer qu'une carte du croupier

total_joueur = jeu.evaluer_main(main_joueur)
total_croupier = jeu.evaluer_main(main_croupier)

print("\nTotal du joueur:", total_joueur)
print("Total du croupier:", total_croupier)