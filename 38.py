"""NOTE: Exercice 1"""


def indices_maxi(tab: list):
    maxi = tab[0]
    indices = []

    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            indices = [i]
        elif tab[i] == maxi:
            indices.append(i)

    return maxi, indices


# (9, [3, 8])
print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))

# (7, [0])
print(indices_maxi([7]))


"""NOTE: Exercice 2"""


def renverse(pile):
    pile_inverse = []

    while pile != []:
        pile_inverse.append(pile.pop())

    return pile_inverse


def positifs(pile):
    pile_positifs = []

    while pile != []:
        el = pile.pop()

        if el >= 0:
            pile_positifs.append(el)

    return renverse(pile_positifs)


# [5, 4, 3, 2, 1]
print(renverse([1, 2, 3, 4, 5]))

# [0, 5, 4, 10, 9]
print(positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]))

# []
print(positifs([-2]))
