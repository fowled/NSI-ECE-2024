"""NOTE: Exercice 1"""


def enumere(tab: list):
    dict = {}

    for i in range(len(tab)):
        if tab[i] in dict:
            dict[tab[i]] += [i]
        else:
            dict[tab[i]] = [i]

    return dict


print(enumere([]))  # {}
print(enumere([1, 2, 3]))  # {1: [0], 2: [1], 3: [2]}
print(enumere([1, 1, 2, 3, 2, 1]))  # {1: [0, 1, 5], 2: [2, 4], 3: [3]}


"""NOTE: Exercice 2"""


class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit


def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)

    return liste


def insere(arbre, cle):
    if arbre == None:
        return Noeud(cle, None, None)
    else:
        if cle < arbre.etiquette:
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle)

        return arbre


A = Noeud(5, Noeud(2, None, Noeud(3, None, None)), Noeud(7, None, None))

print(parcours(A, []))

insere(A, 1)
insere(A, 4)
insere(A, 6)
insere(A, 8)

print(parcours(A, []))
