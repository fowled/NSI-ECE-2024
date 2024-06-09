"""NOTE: Exercice 1"""


def recherche_motif(motif: str, texte: str):
    indices = []

    for i in range(len(texte)):
        if texte[i : i + len(motif)] == motif:
            indices.append(i)

    return indices


print(recherche_motif("ab", ""))  # []
print(recherche_motif("ab", "cdcdcdcd"))  # []
print(recherche_motif("ab", "abracadabra"))  # [0, 7]
print(recherche_motif("ab", "abracadabraab"))  # [0, 7, 11]


"""NOTE: Exercice 2"""


def parcours(adj, x, acc):
    if x not in acc:
        acc.append(x)

        for y in adj[x]:
            parcours(adj, y, acc)


def accessibles(adj, x):
    acc = []

    parcours(adj, x, acc)

    return acc


adj = [[1, 2], [0, 3], [0], [1], [5], [4]]

print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0))  # [0, 1, 2, 3]
print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4))  # [4, 5]
