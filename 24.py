"""NOTE: Exercice 1"""


def parcours_largeur(arbre: tuple):
    parcours = []
    a_visiter = [arbre]

    while len(a_visiter) != 0:
        element = a_visiter.pop(0)
        parcours.append(element[1])

        if element[0] is not None:
            a_visiter.append(element[0])

        if element[2] is not None:
            a_visiter.append(element[2])

    return parcours


arbre = (
    ((None, 1, None), 2, (None, 3, None)),
    4,
    ((None, 5, None), 6, (None, 7, None)),
)

print(parcours_largeur(arbre))


"""NOTE: Exercice 2"""


def somme_max(tab):
    n = len(tab)

    sommes_max = [0] * n
    sommes_max[0] = tab[0]

    for i in range(1, n):
        if sommes_max[i - 1] + tab[i] > tab[i]:
            sommes_max[i] = sommes_max[i - 1] + tab[i]
        else:
            sommes_max[i] = tab[i]

    maximum = 0

    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]:
            maximum = i

    return sommes_max[maximum]


print(somme_max([1, 2, 3, 4, 5]))  # 15
print(somme_max([1, 2, -3, 4, 5]))  # 9
print(somme_max([1, 2, -2, 4, 5]))  # 10
print(somme_max([1, -2, 3, 10, -4, 7, 2, -5]))  # 18
