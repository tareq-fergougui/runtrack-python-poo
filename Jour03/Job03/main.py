class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        self.statut = "terminée"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.marquerCommeFinie()

    def afficherListe(self):
        for tache in self.taches:
            print("Titre :", tache.titre)
            print("Description :", tache.description)
            print("Statut :", tache.statut)
            print("-----------------------")

    def filterListe(self, statut):
        filtered_list = []
        for tache in self.taches:
            if tache.statut == statut:
                filtered_list.append(tache)
        return filtered_list


# Création des tâches
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Appeler le médecin", "Prendre rendez-vous pour un suivi")
tache3 = Tache("Répondre aux e-mails", "Traiter les demandes des clients")

# Création de la liste de tâches
liste_taches = ListeDeTaches()

# Ajout des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de toutes les tâches
print("Liste de toutes les tâches :")
liste_taches.afficherListe()

# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie(tache2)

# Affichage des tâches à faire
print("Liste des tâches à faire :")
taches_a_faire = liste_taches.filterListe("à faire")
for tache in taches_a_faire:
    print("Titre :", tache.titre)
    print("Description :", tache.description)
    print("-----------------------")

# Suppression d'une tâche
liste_taches.supprimerTache(tache1)

# Affichage de toutes les tâches après la suppression
print("Liste de toutes les tâches après la suppression :")
liste_taches.afficherListe()