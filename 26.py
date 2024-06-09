from random import randint


"""NOTE: Exercice 1"""


def ajoute_dictionnaires(d1: dict, d2: dict):
    d = d1

    for valeur in d2:
        if d.get(valeur):
            d[valeur] += d2[valeur]
        else:
            d[valeur] = d2[valeur]

    return d


print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))  # {1: 5, 2: 16, 3: 11}
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))  # {2: 9, 3: 11}
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))  # {1: 5, 2: 7}


"""NOTE: Exercice 2"""


def nombre_coups():
    nombre_cases = 12

    cases_vues = [False] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True

    case_en_cours = 0

    n = 0

    while nombre_cases_vues < nombre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nombre_cases

        if cases_vues[case_en_cours] == False:
            cases_vues[case_en_cours] = True
            nombre_cases_vues += 1

        n += 1

    return n


print(nombre_coups())