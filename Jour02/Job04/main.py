class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0

    def get_nom(self):
        return self.__nom

    def set_nom(self, nouveau_nom):
        self.__nom = nouveau_nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, nouveau_prenom):
        self.__prenom = nouveau_prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def set_numero_etudiant(self, nouveau_numero_etudiant):
        self.__numero_etudiant = nouveau_numero_etudiant

    def get_credits(self):
        return self.__credits

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("Identifiant :", self.__numero_etudiant)
        print("Niveau :", self.__student_eval())

# Instanciation de l'objet représentant l'étudiant John Doe avec le numéro d'étudiant 145
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(20)
john_doe.add_credits(30)
john_doe.add_credits(40)

# Affichage des informations de l'étudiant
john_doe.student_info()

# Affichage du total de crédits
print("Total de crédits :", john_doe.get_credits())