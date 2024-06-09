"""NOTE: Exercice 1"""


def multiplication(n1: int, n2: int):
    resultat = 0

    for i in range(abs(n2)):
        resultat += abs(n1)

    if (n1 < 0 or n2 < 0) and not (n1 < 0 and n2 < 0):
        resultat = -resultat

    return resultat


print(multiplication(3, 5))  # 15
print(multiplication(-4, -8))  # 32
print(multiplication(-2, 6))  # -12
print(multiplication(-2, 0))  # 0


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


print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))  # True
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))  # False
