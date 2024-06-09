"""NOTE: Exercice 1"""


def moyenne(tab: list):
    somme = 0

    for flottant in tab:
        somme += flottant

    return somme / len(tab)


print(moyenne([1.0]))  # 1.0
print(moyenne([1.0, 2.0, 4.0]))  # 2.3333333333333335


"""NOTE: Exercice 2"""


def binaire(a):
    if a == 0:
        return "0"

    bin_a = ""

    while a != 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2

    return bin_a


print(binaire(83))  # '1010011'
print(binaire(6))  # '110'
print(binaire(127))  # '1111111'
print(binaire(0))  # '0'
