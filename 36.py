"""NOTE: Exercice 1"""


def occurrences(caractere: str, chaine: str):
    compteur = 0

    for char in chaine:
        if char == caractere:
            compteur += 1

    return compteur


print(occurrences("e", "sciences"))  # 2
print(occurrences("i", "mississippi"))  # 4
print(occurrences("a", "mississippi"))  # 0


"""NOTE: Exercice 2"""

valeurs = [100, 50, 20, 10, 5, 2, 1]


def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []

    v = valeurs[rang]

    if v <= a_rendre:
        return [v] + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang + 1)


print(rendu_glouton(67, 0))  # [50, 10, 5, 2]
print(rendu_glouton(291, 0))  # [100, 100, 50, 20, 20, 1]
print(rendu_glouton(291, 1))  # [50, 50, 50, 50, 50, 20, 20, 1]
