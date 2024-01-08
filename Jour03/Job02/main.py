class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.numero_compte = numero_compte
        self.nom = nom
        self.prenom = prenom
        self.solde = solde
        self.decouvert = decouvert

    def afficher(self):
        print("Numéro de compte :", self.numero_compte)
        print("Nom :", self.nom)
        print("Prénom :", self.prenom)
        print("Solde :", self.solde)

    def afficherSolde(self):
        print("Solde du client :", self.solde)

    def versement(self, montant):
        self.solde += montant
        print("Versement de", montant, "effectué. Nouveau solde :", self.solde)

    def retrait(self, montant):
        if self.solde - montant >= 500 or self.decouvert:
            self.solde -= montant
            print("Retrait de", montant, "effectué. Nouveau solde :", self.solde)
        else:
            print("Solde insuffisant. Retrait impossible.")

    def agios(self):
        if self.solde < 0:
            agios = self.solde * 0.05  # Exemple d'application d'agios de 5%
            self.solde += agios
            print("Des agios de", agios, "ont été appliqués. Nouveau solde :", self.solde)

    def virement(self, compte_dest, montant):
        if self.solde - montant >= 600 or self.decouvert:
            self.solde -= montant
            compte_dest.solde += montant
            print("Virement de", montant, "effectué vers le compte", compte_dest.numero_compte)
            print("Nouveau solde du compte :", self.solde)
        else:
            print("Solde insuffisant. Virement impossible.")


# Création du premier compte bancaire
compte1 = CompteBancaire("123456789", "Fergougui", "Tareq", 1000)

# Appel des différentes méthodes
compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(200)
compte1.agios()

# Création du deuxième compte bancaire à découvert
compte2 = CompteBancaire("987654321", "Martin", "Sophie", -500, decouvert=True)

# Virement du premier compte vers le deuxième compte pour le remettre à zéro
compte1.virement(compte2, compte1.solde)

# Affichage des comptes après le virement
compte1.afficher()
compte2.afficher()