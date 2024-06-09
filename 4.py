"""NOTE: Exercice 1"""


def recherche(tab: list, n: int):
    indice = None

    for i in range(len(tab)):
        if tab[i] == n:
            indice = i

    return indice


print(recherche([5, 3], 1))  #  None
print(recherche([2, 4], 2))  # 0
print(recherche([2, 3, 5, 2, 4], 2))  # 3


"""NOTE: Exercice 2"""


def distance_carre(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def point_le_plus_proche(depart, tab):
    min_point = tab[0]
    min_dist = distance_carre(min_point, depart)

    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < min_dist:
            min_point = tab[i]
            min_dist = distance_carre(min_point, depart)

    return min_point


print(distance_carre((1, 0), (5, 3)))  # 25
print(distance_carre((1, 0), (0, 1)))  # 2
print(point_le_plus_proche((0, 0), [(7, 9), (2, 5), (5, 2)]))  # (2, 5)
print(point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)]))  # (5, 2)
