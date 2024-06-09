"""NOTE: Exercice 1"""


def compte_occurrences(x: str | int, tab: list):
    compteur = 0

    for valeur in tab:
        if valeur == x:
            compteur += 1

    return compteur


print(compte_occurrences(5, []))  # 0
print(compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]))  # 1
print(compte_occurrences("a", ["a", "b", "c", "a", "d", "e", "a"]))  # 3


"""NOTE: Exercice 2"""

pieces = [1, 2, 5, 10, 20, 50, 100, 200]


def rendu_monnaie(somme_due, somme_versee):
    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1

    while a_rendre > 0:
        while pieces[i] > a_rendre:
            i = i - 1

        rendu.append(pieces[i])
        a_rendre -= pieces[i]

    return rendu


print(rendu_monnaie(700, 700))  # []
print(rendu_monnaie(102, 500))  # [200, 100, 50, 20, 20, 5, 2, 1]
