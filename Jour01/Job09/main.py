class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print(f"Produit : {self.nom}\n"
              f"Prix HT : {self.prixHT} €\n"
              f"TVA : {self.TVA}%\n"
              f"Prix TTC : {self.CalculerPrixTTC()} €")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit("Livre", 15.99, 5)
produit2 = Produit("Ordinateur", 899.99, 20)

# Affichage des informations initiales
produit1.afficher()
produit2.afficher()

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Nouveau Livre")
produit1.modifierPrixHT(19.99)

produit2.modifierNom("Nouvel Ordinateur")
produit2.modifierPrixHT(999.99)

# Affichage des informations après modification
print("\nAprès modification :\n")
produit1.afficher()
produit2.afficher()
