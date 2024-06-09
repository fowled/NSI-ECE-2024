"""NOTE: Exercice 1"""


def min_et_max(tab: list):
    min = tab[0]
    max = tab[0]

    for entier in tab:
        if entier > max:
            max = entier

        if entier < min:
            min = entier

    return {"min": min, "max": max}


print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))  # {'min': -2, 'max': 9}
print(min_et_max([0, 1, 2, 3]))  # {'min': 0, 'max': 3}
print(min_et_max([3]))  # {'min': 3, 'max': 3}
print(min_et_max([1, 3, 2, 1, 3]))  # {'min': 1, 'max': 3}
print(min_et_max([-1, -1, -1, -1, -1]))  # {'min': -1, 'max': -1}


"""NOTE: Exercice 2"""


class Carte:
    def __init__(self, c, v):
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        valeurs = [
            "As",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Valet",
            "Dame",
            "Roi",
        ]

        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        couleurs = ["pique", "coeur", "carreau", "trèfle"]

        return couleurs[self.couleur - 1]


class Paquet_de_cartes:
    def __init__(self):
        self.contenu = []

        for k in range(1, 5):
            for i in range(1, 14):
                self.contenu.append(Carte(k, i))

    def recuperer_carte(self, pos):
        """Renvoie la carte qui se trouve à la position pos
        (entier compris entre 0 et 51)."""
        assert 0 <= pos <= 51, "L'entier n'est pas compris entre 0 et 51"

        return self.contenu[pos]


jeu = Paquet_de_cartes()

carte1 = jeu.recuperer_carte(20)
print(carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur())  # "8 de coeur"

carte2 = jeu.recuperer_carte(0)
print(carte2.recuperer_valeur() + " de " + carte2.recuperer_couleur())  # "As de pique"

carte3 = jeu.recuperer_carte(52)  # AssertionError : paramètre pos invalide
