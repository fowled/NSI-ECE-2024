"""NOTE: Exercice 1"""

arbre = {
    "F": ["B", "G"],
    "B": ["A", "D"],
    "A": ["", ""],
    "D": ["C", "E"],
    "C": ["", ""],
    "E": ["", ""],
    "G": ["", "I"],
    "I": ["", "H"],
    "H": ["", ""],
}


def taille(arbre: dict, lettre: str):
    if arbre.get(lettre) is None:
        return 0

    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])


print(taille(arbre, "F"))  # 9
print(taille(arbre, "B"))  # 5
print(taille(arbre, "I"))  # 2

"""NOTE: Exercice 2"""

tab = [41, 55, 21, 18, 12, 6, 25]


def echange(tab, i, j):
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def tri_selection(tab):
    N = len(tab)

    for k in range(N):
        imin = k

        for i in range(k + 1, N):
            if tab[i] < tab[imin]:
                imin = i

        echange(tab, k, imin)


tri_selection(tab)
print(tab)  # [6, 12, 18, 21, 25, 41, 55]
