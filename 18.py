"""NOTE: Exercice 1"""


def multiplication(n1: int, n2: int):
    addition = 0

    for i in range(abs(n2)):
        addition += abs(n1)

    if (n1 < 0 or n2 < 0) and not (n1 < 0 and n2 < 0):
        addition = -addition

    return addition


print(multiplication(3, 5))  # 15
print(multiplication(-4, -8))  # 32
print(multiplication(-2, 6))  # -12
print(multiplication(-2, 0))  # 0


"""NOTE: Exercice 2"""


def chercher(tab, x, i, j):
    if i > j:
        return None
    
    m = (i + j) // 2

    if tab[m] < x:
        return chercher(tab, x, m + 1, j)
    elif tab[m] > x:
        return chercher(tab, x, i, m - 1)
    else:
        return m


print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))  # None
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))  # None
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))  # 4
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))  # 2
