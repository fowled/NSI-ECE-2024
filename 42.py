"""NOTE: Exercice 1"""


def moyenne(tab: list):
    moyenne = 0

    for entier in tab:
        moyenne += entier

    return moyenne / len(tab)


print(moyenne([1]))  # 1.0
print(moyenne([1, 2, 3, 4, 5, 6, 7]))  # 4.0
print(moyenne([1, 2]))  # 1.5


"""NOTE: Exercice 2"""


def dichotomie(tab, x):
    debut = 0
    fin = len(tab) - 1

    while debut <= fin:
        m = (debut + fin) // 2

        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1

    return False


# True
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))

# False
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))

# False
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))

# False
print(dichotomie([], 28))
