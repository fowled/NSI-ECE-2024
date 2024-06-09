"""NOTE: Exercice 1"""


def max_et_indice(tab: list):
    max = tab[0]
    indice = 0

    for i in range(1, len(tab)):
        if tab[i] > max:
            max = tab[i]
            indice = i

    return max, indice


print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))  # (9, 3)
print(max_et_indice([-2]))  # (-2, 0)
print(max_et_indice([-1, -1, 3, 3, 3]))  # (3, 2)
print(max_et_indice([1, 1, 1, 1]))  # (1, 0)


"""NOTE: Exercice 2"""


def est_un_ordre(tab):
    n = len(tab)
    vus = []

    for x in tab:
        if x < 1 or x > n or x in vus:
            return False

        vus.append(x)

    return True


def nombre_points_rupture(ordre):
    assert est_un_ordre(ordre)

    n = len(ordre)
    nb = 0

    if ordre[0] != 1:
        nb = nb + 1

    i = 0

    while i < n - 1:
        if ordre[i + 1] - ordre[i] not in [-1, 1]:
            nb = nb + 1

        i = i + 1

    if ordre[i] != n:
        nb = nb + 1

    return nb


print(est_un_ordre([1, 6, 2, 8, 3, 7]))  # False
print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))  # True

print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))  # 4
print(nombre_points_rupture([1, 2, 3, 4, 5]))  # 0
print(nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]))  # 7
print(nombre_points_rupture([2, 1, 3, 4]))  # 2
