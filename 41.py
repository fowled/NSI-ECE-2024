"""NOTE: Exercice 1"""


class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit


def taille(arbre: Noeud):
    if arbre is None:
        return 0

    return 1 + taille(arbre.droit) + taille(arbre.gauche)


def hauteur(arbre: Noeud):
    if arbre is None:
        return -1

    return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))


a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

print(hauteur(a))  # 2
print(taille(a))  # 4
print(hauteur(None))  # -1
print(taille(None))  # 0
print(hauteur(Noeud(1, None, None)))  # 0
print(taille(Noeud(1, None, None)))  # 1


"""NOTE: Exercice 2"""


def ajoute(indice, element, tab):
    """Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab."""
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)

    for i in range(indice):
        tab_ins[i] = tab[i]

    tab_ins[indice] = element

    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i - 1]

    return tab_ins


print(ajoute(1, 4, [7, 8, 9]))  # [7, 4, 8, 9]
print(ajoute(3, 4, [7, 8, 9]))  # [7, 8, 9, 4]
print(ajoute(0, 4, [7, 8, 9]))  # [4, 7, 8, 9]
