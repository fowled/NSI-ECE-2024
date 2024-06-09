"""NOTE: Exercice 1"""


def moyenne_ponderee(notes):
    numerateur = 0
    denominateur = 0

    for note in notes:
        numerateur += note[0] * note[1]
        denominateur += note[1]

    if denominateur == 0:
        return None

    return numerateur / denominateur


# 9.142857142857142
print(moyenne_ponderee([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))

# None
print(moyenne_ponderee([(3, 0), (5, 0)]))


"""NOTE: Exercice 2"""
coeur = [
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
]


def affiche(dessin):
    """affichage d'une grille : les 1 sont représentés par
    des "*" , les 0 par un espace " " """
    for ligne in dessin:
        affichage = ""

        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "

        print(affichage)


def liste_zoom(liste_depart, k):
    liste_zoomee = []

    for elt in liste_depart:
        for i in range(k):
            liste_zoomee.append(elt)

    return liste_zoomee


def dessin_zoom(grille, k):
    grille_zoomee = []

    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne, k)

        for i in range(k):
            grille_zoomee.append(ligne_zoomee)

    return grille_zoomee


affiche(coeur)

# [1, 1, 1, 2, 2, 2, 3, 3, 3]
print(liste_zoom([1, 2, 3], 3))

affiche(dessin_zoom(coeur, 2))
