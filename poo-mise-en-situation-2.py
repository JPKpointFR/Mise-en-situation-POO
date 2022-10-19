# POO EXERCICE DE MISE EN SITUATION 2
class Personne:
    def __init__(self, nom, age):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        print(f"Constructeur personne {self.nom}")

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur

        print(f"Bonjour, je m'appelle {self.nom} j'ai {self.age} ans")
        print("Je suis majeur") if self.age >= 18 else print("Je suis mineur")

        # if self.EstMajeur():
        #     print("Je suis majeur")
        # else:
        #     print("Je suis mineur")
        # print()

    # def EstMajeur(self):
    #     return self.age >= 18


personne1 = Personne("Jean", 25)
personne2 = Personne("Emilie", 17)

personne1.SePresenter()
personne2.SePresenter()
