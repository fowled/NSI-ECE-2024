"""NOTE: Exercice 1"""


def a_doublon(tab: list):
    for i in range(len(tab) - 1):
        if tab[i] == tab[i + 1]:
            return True

    return False


print(a_doublon([]))  # False
print(a_doublon([1]))  # False
print(a_doublon([1, 2, 4, 6, 6]))  # True
print(a_doublon([2, 5, 7, 7, 7, 9]))  # True
print(a_doublon([0, 2, 3]))  # False


"""NOTE: Exercice 2"""


def voisinage(n, ligne, colonne):
    voisins = []

    for l in range(max(0, ligne - 1), min(n, ligne + 2)):
        for c in range(max(0, colonne - 1), min(n, colonne + 2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l, c))

    return voisins


def incremente_voisins(grille, ligne, colonne):
    voisins = voisinage(len(grille), ligne, colonne)

    for l, c in voisins:
        if grille[l][c] != -1:
            grille[l][c] += 1


def genere_grille(bombes):
    n = len(bombes)

    grille = [[0 for colonne in range(n)] for ligne in range(n)]

    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1
        incremente_voisins(grille, ligne, colonne)

    return grille


"""[
    [1, 1, 1, 0, 0],
    [1, -1, 1, 1, 1],
    [2, 2, 3, 2, -1],
    [1, -1, 2, -1, 3],
    [1, 1, 2, 2, -1],
]"""
print(genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]))
