"""NOTE: Exercice 1"""


def insertion_abr(a: tuple, cle: int):
    if a is None:
        return (None, cle, None)
    elif cle > a[1]:
        return (a[0], a[1], insertion_abr(a[2], cle))
    elif cle < a[1]:
        return (insertion_abr(a[0], cle), a[1], a[2])
    elif cle == a[1]:
        return a


n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)

abr1 = (n0, 1, n2)

# ((None,0,None),1,(None,2,(None,3,(None,4,None))))
print(insertion_abr(abr1, 4))

# (((None,-5,None),0,None),1,(None,2,(None,3,None)))
print(insertion_abr(abr1, -5))

# ((None,0,None),1,(None,2,(None,3,None)))
print(insertion_abr(abr1, 2))


"""NOTE: Exercice 2"""


def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0 for _ in range(n)]

    for masse in liste_masses:
        i = 0

        while i < nb_boites and boites[i] + masse > c:
            i = i + 1

        if i == nb_boites:
            nb_boites += 1

        boites[i] += masse

    return nb_boites


print(empaqueter([1, 2, 3, 4, 5], 10))  # 2
print(empaqueter([1, 2, 3, 4, 5], 5))  # 4
print(empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11))  # 5
