"""NOTE: Exercice 1"""


def nb_repetitions(elt: int | str, tab: list):
    compteur = 0

    for element in tab:
        if element == elt:
            compteur += 1

    return compteur


print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))  # 3
print(nb_repetitions("A", ["B", "A", "B", "A", "R"]))  # 2
print(nb_repetitions(12, [1, 3, 7, 21, 36, 44]))  # 0


"""NOTE: Exercice 2"""


def binaire(a):
    if a == 0:
        return "0"

    bin_a = ""

    while a != 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2

    return bin_a


print(binaire(0))  # '0'
print(binaire(77))  # '1001101'
