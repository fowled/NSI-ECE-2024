"""NOTE: Exercice 1"""


def gb_vers_entier(tab: list):
    somme = 0

    for i in range(len(tab)):
        if tab[i] == True:
            somme += 2 ** ((len(tab) - 1) - i)

    return somme


print(gb_vers_entier([]))  # 0
print(gb_vers_entier([True]))  # 1
print(gb_vers_entier([True, False, True, False, False, True, True]))  # 83
print(gb_vers_entier([True, False, False, False, False, False, True, False]))  # 130


"""NOTE: Exercice 2"""


def tri_insertion(tab):
    n = len(tab)

    for i in range(1, n):
        valeur_insertion = tab[i]

        j = i

        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j - 1]
            j -= 1

        tab[j] = valeur_insertion


tab = [98, 12, 104, 23, 131, 9]
tri_insertion(tab)
print(tab)  # [9, 12, 23, 98, 104, 131]
