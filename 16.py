"""NOTE: Exercice 1"""


def ecriture_binaire_entier_positif(entier: int):
    reste = ""

    while entier > 1:
        reste = str(entier % 2) + reste
        entier //= 2

    reste = str(entier % 2) + reste

    return reste


print(ecriture_binaire_entier_positif(0))  # 0
print(ecriture_binaire_entier_positif(2))  # 10
print(ecriture_binaire_entier_positif(105))  # 1101001


"""NOTE: Exercice 2"""


def echange(tab, i, j):
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def tri_bulles(tab):
    n = len(tab)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tab[j] > tab[j + 1]:
                echange(tab, j, j + 1)


tab = []
tri_bulles(tab)
print(tab)  # []

tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
print(tab2)  # [1, 2, 3, 3, 6, 7, 9]

tab3 = [9, 7, 4, 3]
tri_bulles(tab3)
print(tab3)  # [3, 4, 7, 9]
