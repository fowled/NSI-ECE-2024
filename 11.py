"""NOTE: Exercice 1"""


def nombre_de_mots(phrase: str):
    compteur = 0

    mots = phrase.split(" ")

    for mot in mots:
        if mot != "?" and mot != "!":
            compteur += 1

    return compteur


print(nombre_de_mots("Cet exercice est simple."))  # 4
print(nombre_de_mots("Le point d exclamation est séparé !"))  # 6
print(nombre_de_mots("Combien de mots y a t il dans cette phrase ?"))  # 10
print(nombre_de_mots("Fin."))  # 1


"""NOTE: Exercice 2"""


class Noeud:
    def __init__(self, etiquette):
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)


arbre = Noeud(7)

for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

print(arbre.gauche.etiquette)  # 3
print(arbre.droit.etiquette)  # 9
print(arbre.gauche.gauche.etiquette)  # 1
print(arbre.gauche.droit.etiquette)  # 6
