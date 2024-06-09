"""NOTE: Exercice 1"""


def moyenne(tab: list):
    if tab == []:
        return None

    moyenne = 0

    for entier in tab:
        moyenne += entier

    return moyenne / len(tab)


print(moyenne([5, 3, 8]))  # 5.333333333333333
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 5.5
print(moyenne([]))  # None


"""NOTE: Exercice 2"""


def tri(tab):
    i = 0
    j = len(tab) - 1

    while i < j:
        if tab[i] == 0:
            i = i + 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur

            j = j - 1


tab = [0, 1, 0, 1, 0, 1, 0, 1, 0]
tri(tab)
print(tab)  # [0, 0, 0, 0, 0, 1, 1, 1, 1]
