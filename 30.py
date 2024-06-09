"""NOTE: Exercice 1"""


def fusion(tab1: list, tab2: list):
    resultat = []
    i, j = 0, 0

    while i < len(tab1) and j < len(tab2):
        if tab1[i] <= tab2[j]:
            resultat.append(tab1[i])
            i += 1
        else:
            resultat.append(tab2[i])
            j += 1

    resultat.extend(tab1[i:])
    resultat.extend(tab2[j:])

    return resultat


print(fusion([3, 5], [2, 5]))  # [2, 3, 5, 5]
print(fusion([-2, 4], [-3, 5, 10]))  # [-3, -2, 4, 5, 10]
print(fusion([4], [2, 6]))  # [2, 4, 6]
print(fusion([], []))  # []
print(fusion([1, 2, 3], []))  # [1, 2, 3]

"""NOTE: Exercice 2"""

romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def traduire_romain(nombre):
    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]


print(traduire_romain("XIV"))  # 14
print(traduire_romain("CXLII"))  # 142
print(traduire_romain("MMXXIV"))  # 2024
