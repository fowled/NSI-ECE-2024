"""NOTE: Exercice 1"""


def liste_puissances(a: int, n: int):
    puissances = []
    valeur = a

    for i in range(n):
        puissances.append(valeur)
        valeur *= a

    return puissances


def liste_puissances_borne(a: int, borne: int):
    puissances = []
    valeur = a

    while valeur < borne:
        puissances.append(valeur)
        valeur *= a

    return puissances


print(liste_puissances(3, 5))  # [3, 9, 27, 81, 243]
print(liste_puissances(-2, 4))  # [-2, 4, -8, 16]

print(liste_puissances_borne(2, 16))  # [2, 4, 8]
print(liste_puissances_borne(2, 17))  # [2, 4, 8, 16]
print(liste_puissances_borne(5, 5))  # []


"""NOTE: Exercice 2"""

dico = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


def codes_parfait(mot: str):
    code_concatene = ""
    code_additionne = 0

    for c in mot:
        code_concatene += str(dico[c])
        code_additionne += dico[c]

    code_concatene = int(code_concatene)
    mot_est_parfait = code_concatene % code_additionne == 0

    return code_additionne, code_concatene, mot_est_parfait


print(codes_parfait("PAUL"))  # (50, 1612112, False)
print(codes_parfait("ALAIN"))  # (37, 1121914, True)
