"""NOTE: Exercice 1"""

animaux = [
    {"nom": "Medor", "espece": "chien", "age": 5, "enclos": 2},
    {"nom": "Titine", "espece": "chat", "age": 2, "enclos": 5},
    {"nom": "Tom", "espece": "chat", "age": 7, "enclos": 4},
    {"nom": "Belle", "espece": "chien", "age": 6, "enclos": 3},
    {"nom": "Mirza", "espece": "chat", "age": 6, "enclos": 5},
]


def selection_enclos(table: list, num_enclos: int):
    resultat = []

    for animal in table:
        if animal["enclos"] == num_enclos:
            resultat.append(animal)

    return resultat


# [{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5}, {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
print(selection_enclos(animaux, 5))

# [{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}]
print(selection_enclos(animaux, 2))

# []
print(selection_enclos(animaux, 7))


"""NOTE: Exercice 2"""


def trouver_intrus(tab, g, d):
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)

        if tab[indice] != tab[indice + 1]:
            return trouver_intrus(tab, g, indice)
        else:
            return trouver_intrus(tab, indice + 3, d)


# 7
print(trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8], 0, 18))

# 8
print(trouver_intrus([8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3], 0, 12))

# 3
print(trouver_intrus([5, 5, 5, 1, 1, 1, 0, 0, 0, 6, 6, 6, 3, 8, 8, 8], 0, 15))
