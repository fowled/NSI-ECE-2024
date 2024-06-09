"""NOTE: Exercice 1"""


def recherche(elt: int, tab: list):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i

    return None


print(recherche(1, [2, 3, 4]))  # None
print(recherche(1, [10, 12, 1, 56]))  # 2
print(recherche(50, [1, 50, 1]))  # 1
print(recherche(15, [8, 9, 10, 15]))  # 3


"""NOTE: Exercice 2"""


def insere(tab, a):
    tab_a = [a] + tab
    i = 0

    while i < len(tab) and a > tab[i]:
        tab_a[i] = tab_a[i + 1]
        tab_a[i + 1] = a
        i = i + 1

    return tab_a


print(insere([1, 2, 4, 5], 3))  # [1, 2, 3, 4, 5]
print(insere([1, 2, 7, 12, 14, 25], 30))  # [1, 2, 7, 12, 14, 25, 30]
print(insere([2, 3, 4], 1))  # [1, 2, 3, 4]
print(insere([], 1))  # [1]
