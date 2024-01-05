class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix, "statut": self.__statut_commande}
            print("Plat ajouté à la commande :", nom_plat)
        else:
            print("Ce plat est déjà présent dans la commande.")

    def annuler_commande(self):
        self.__statut_commande = "annulée"
        self.__plats_commandes = {}
        print("La commande a été annulée.")

    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes.values():
            if plat["statut"] != "annulée":
                total += plat["prix"]
        return total

    def afficher_commande(self):
        print("Numéro de commande :", self.__numero_commande)
        print("Liste des plats commandés :")
        for nom_plat, plat in self.__plats_commandes.items():
            print(nom_plat, "- Prix :", plat["prix"], "- Statut :", plat["statut"])
        print("Total à payer :", self.__calculer_total())

    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * (taux_tva / 100)
        return tva

# Création d'un objet représentant une commande avec le numéro de commande 123
ma_commande = Commande(123)

# Ajout de plats à la commande
ma_commande.ajouter_plat("Pizza", 10.0)
ma_commande.ajouter_plat("Burger", 8.0)
ma_commande.ajouter_plat("Salade", 5.0)

# Annulation de la commande
ma_commande.annuler_commande()

# Affichage de la commande
ma_commande.afficher_commande()

# Calcul de la TVA avec un taux de 20%
tva = ma_commande.calculer_tva(20)
print("TVA :", tva)