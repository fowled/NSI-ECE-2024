"""NOTE: Exercice 1"""


def voisins_entrants(adj: list, x: int):
    voisins = []

    for i in range(len(adj)):
        for valeur in adj[i]:
            if valeur == x:
                voisins.append(i)

    return voisins


print(voisins_entrants([[1, 2], [2], [0], [0]], 0))  # [2, 3]
print(voisins_entrants([[1, 2], [2], [0], [0]], 1))  # [0]


"""NOTE: Exercice 2"""


def nombre_suivant(s):
    resultat = ""
    chiffre = s[0]
    compte = 1

    for i in range(1, len(s)):
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + str(chiffre)
            chiffre = s[i]
            compte = 1

    lecture_chiffre = str(compte) + str(chiffre)
    resultat += lecture_chiffre

    return resultat


print(nombre_suivant("1211"))  # '111221'
print(nombre_suivant("311"))  # '1321'
