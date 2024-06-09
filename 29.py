"""NOTE: Exercice 1"""


def moyenne(notes: list):
    numerateur = 0
    denominateur = 0

    for note, coefficient in notes:
        numerateur += note * coefficient
        denominateur += coefficient

    return numerateur / denominateur


print(moyenne([(15.0, 2), (9.0, 1), (12.0, 3)]))  # 12.5


"""NOTE: Exercice 2"""


def ligne_suivante(ligne):
    ligne_suiv = [1]

    for i in range(1, len(ligne)):
        ligne_suiv.append(ligne[i - 1] + ligne[i])

    ligne_suiv.append(1)

    return ligne_suiv


def pascal(n):
    triangle = [[1]]

    for k in range(n):
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)

    return triangle


print(ligne_suivante([1, 3, 3, 1]))  # [1, 4, 6, 4, 1]
print(pascal(2))  # [[1], [1, 1], [1, 2, 1]]
print(pascal(3))  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
