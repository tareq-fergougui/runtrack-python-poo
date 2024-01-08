class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print("Statistiques de", self.nom)
        print("Numéro :", self.numero)
        print("Position :", self.position)
        print("Buts marqués :", self.buts_marques)
        print("Passes décisives :", self.passes_decisives)
        print("Cartons jaunes reçus :", self.cartons_jaunes)
        print("Cartons rouges reçus :", self.cartons_rouges)
        print("-----------------------")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print("Statistiques des joueurs de l'équipe", self.nom)
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        joueur.buts_marques += buts
        joueur.passes_decisives += passes_decisives
        joueur.cartons_jaunes += cartons_jaunes
        joueur.cartons_rouges += cartons_rouges


# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Modric", 10, "Milieu de terrain")

# Création des équipes
equipe1 = Equipe("Barcelone")
equipe2 = Equipe("Al-Nassr")
equipe3 = Equipe("Real Madrid")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

# Affichage des statistiques des joueurs avant le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation d'un match
joueur1.marquerUnBut()
joueur1.marquerUnBut()
joueur2.marquerUnBut()
joueur3.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()

# Mise à jour des statistiques des joueurs
equipe1.mettreAJourStatistiquesJoueur(joueur1, buts=1, passes_decisives=2)
equipe2.mettreAJourStatistiquesJoueur(joueur2, buts=20, passes_decisives=9, cartons_jaunes=1)
equipe3.mettreAJourStatistiquesJoueur(joueur3, buts=1, passes_decisives=4, cartons_jaunes=1)

# Affichage des statistiques des joueurs après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()