"""NOTE: Exercice 1"""


def recherche(elt: int, tab: list):
    indice = None

    for i in range(len(tab)):
        if tab[i] == elt:
            indice = i

    return indice


print(recherche(1, [2, 3, 4]))  # None
print(recherche(1, [10, 12, 1, 56]))  # 2
print(recherche(1, [1, 0, 42, 7]))  # 0
print(recherche(1, [1, 50, 1]))  # 2
print(recherche(1, [8, 1, 10, 1, 7, 1, 8]))  # 5


"""NOTE: Exercice 2"""


class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octets(self):
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        reservees = ["192.168.0.0", "192.168.0.255"]

        return self.adresse in reservees

    def adresse_suivante(self):
        octets = self.liste_octets()

        if octets[-1] == 254:
            return None

        octet_nouveau = octets[-1] + 1

        return AdresseIP("192.168.0." + str(octet_nouveau))


adresse1 = AdresseIP("192.168.0.1")
adresse2 = AdresseIP("192.168.0.2")
adresse3 = AdresseIP("192.168.0.0")

print(adresse1.liste_octets())  # [192, 168, 0, 1]
print(adresse1.est_reservee())  # False
print(adresse3.est_reservee())  # True
print(adresse2.adresse_suivante().adresse)  # '192.168.0.3'
