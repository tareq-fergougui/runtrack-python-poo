class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_nombre_pages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

# Création d'un livre avec les valeurs initiales
mon_livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 500)

# Affichage des valeurs initiales
print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nombre_pages())

# Modification des valeurs
mon_livre.set_titre("Harry Potter")
mon_livre.set_auteur("J.K. Rowling")
mon_livre.set_nombre_pages(700)

# Affichage des nouvelles valeurs
print("Nouveau titre :", mon_livre.get_titre())
print("Nouvel auteur :", mon_livre.get_auteur())
print("Nouveau nombre de pages :", mon_livre.get_nombre_pages())

# Tentative de modification du nombre de pages avec une valeur invalide
mon_livre.set_nombre_pages(-100)  # Affiche un message d'erreur