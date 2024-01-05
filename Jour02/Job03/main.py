class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True

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

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté.")

# Création d'un livre avec les valeurs initiales
mon_livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 500)

# Vérification de disponibilité
print("Disponibilité :", mon_livre.verification())

# Emprunt du livre
mon_livre.emprunter()

# Vérification de disponibilité après emprunt
print("Disponibilité :", mon_livre.verification())

# Rendre le livre
mon_livre.rendre()

# Vérification de disponibilité après rendu
print("Disponibilité :", mon_livre.verification())