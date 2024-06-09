"""NOTE: Exercice 1"""


def recherche(tab: list, n: int):
    debut = 0
    fin = len(tab) - 1

    while debut <= fin:
        moitie = (debut + fin) // 2

        if tab[moitie] == n:
            return moitie
        elif tab[moitie] < n:
            debut = moitie + 1
        elif tab[moitie] > n:
            fin = moitie - 1

    return None


print(recherche([2, 3, 4, 5, 6], 5))  # 3
print(recherche([2, 3, 4, 6, 7], 5))  # None


"""NOTE: Exercice 2"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def position_alphabet(lettre):
    return ord(lettre) - ord("A")


def cesar(message, decalage):
    resultat = ""

    for c in message:
        if "A" <= c and c <= "Z":
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c

    return resultat


# 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
print(cesar("BONJOUR A TOUS. VIVE LA MATIERE NSI !", 4))

# 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
print(cesar("GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !", -5))
