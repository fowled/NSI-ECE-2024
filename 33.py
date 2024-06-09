"""NOTE: Exercice 1"""


def renverse(mot: str):
    resultat = ""

    for lettre in mot:
        resultat = lettre + resultat

    return resultat


print(renverse(""))
print(renverse("abc"))
print(renverse("informatique"))


"""NOTE: Exercice 2"""


def crible(n):
    premiers = []

    tab = [True] * n
    tab[0], tab[1] = False, False

    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = 2 * i

            while multiple < n:
                tab[multiple] = False
                multiple = multiple + i

    return premiers


# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
print(crible(40))

# [2, 3]
print(crible(5))
