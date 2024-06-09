"""NOTE: Exercice 1"""


def recherche_min(tab: list):
    indice = 0
    mini = tab[indice]

    for i in range(1, len(tab)):
        if tab[i] < mini:
            indice = i
            mini = tab[indice]

    return indice


print(recherche_min([5]))  # 0
print(recherche_min([2, 4, 1]))  # 2
print(recherche_min([5, 3, 2, 2, 4]))  # 2
print(recherche_min([-1, -2, -3, -3]))  # 2


"""NOTE: Exercice 2"""


def separe(tab):
    gauche = 0
    droite = len(tab) - 1

    while gauche < droite:
        if tab[gauche] == 0:
            gauche += 1
        else:
            tab[gauche] = tab[droite]
            tab[droite] = 1

            droite -= 1

    return tab


# [0, 0, 0, 0, 1, 1, 1, 1]
print(separe([1, 0, 1, 0, 1, 0, 1, 0]))

# [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]))
