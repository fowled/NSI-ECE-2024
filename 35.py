"""NOTE: Exercice 1"""


def annee_temperature_minimale(t_moy: list, annees: list):
    temperature_min = t_moy[0]
    annee_min = annees[0]

    for i in range(1, len(t_moy)):
        if t_moy[i] < temperature_min:
            temperature_min = t_moy[i]
            annee_min = annees[i]

    return temperature_min, annee_min


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(annee_temperature_minimale(t_moy, annees))  # (12.5, 2016)


"""NOTE: Exercice 2"""


def inverse_chaine(chaine):
    resultat = ""

    for caractere in chaine:
        resultat = caractere + resultat

    return resultat


def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)

    return inverse == chaine


def est_nbre_palindrome(nbre):
    chaine = str(nbre)

    return est_palindrome(chaine)


print(inverse_chaine("bac"))  # 'cab'

print(est_palindrome("NSI"))  # False
print(est_palindrome("ISN-NSI"))  # True

print(est_nbre_palindrome(214312))  # False
print(est_nbre_palindrome(213312))  # True
