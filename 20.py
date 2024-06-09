from random import randint

"""NOTE: Exercice 1"""


def lancer(n: int):
    return [randint(1, 6) for _ in range(n)]


def paire_6(tab: list):
    compteur = 0

    for entier in tab:
        if entier == 6:
            compteur += 1

    return compteur >= 2


lancer1 = lancer(5)
print(lancer1)

print(paire_6(lancer1))


"""NOTE: Exercice 2"""


def nombre_lignes(image):
    return len(image)


def nombre_colonnes(image):
    return len(image[0])


def negatif(image):
    nouvelle_image = [
        [0 for k in range(nombre_colonnes(image))] for i in range(nombre_lignes(image))
    ]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)):
            nouvelle_image[i][j] = 255 - image[i][j]

    return nouvelle_image


def binaire(image, seuil):
    """renvoie une image binarisee de l'image sous la forme
    d'une liste de listes contenant des 0 si la valeur
    du pixel est strictement inferieure au seuil et 1 sinon"""
    nouvelle_image = [[0] * nombre_colonnes(image) for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)):
            if image[i][j] < seuil:
                nouvelle_image[i][j] = 0
            else:
                nouvelle_image[i][j] = 1

    return nouvelle_image


img = [
    [20, 34, 254, 145, 6],
    [23, 124, 237, 225, 69],
    [197, 174, 207, 25, 87],
    [255, 0, 24, 197, 189],
]

print(nombre_lignes(img))  # 4

print(nombre_colonnes(img))  # 5

# [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
print(negatif(img))

# [[0, 0, 1, 1, 0],[0, 1, 1, 1, 0],[1, 1, 1, 0, 0],[1, 0, 0, 1, 1]]
print(binaire(img, 120))
