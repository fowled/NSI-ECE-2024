"""NOTE: Exercice 1"""


def maximum_tableau(tab: list):
    maxi = tab[0]

    for i in range(1, len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]

    return maxi


print(maximum_tableau([98, 12, 104, 23, 131, 9]))  # 131
print(maximum_tableau([-27, 24, -3, 15]))  # 24


"""NOTE: Exercice 2"""


class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return self.contenu == []

    def empiler(self, v):
        self.contenu.append(v)

    def depiler(self):
        assert not self.est_vide()
        return self.contenu.pop()


def bon_parenthesage(ch):
    """Renvoie un booléen indiquant si la chaîne ch
    est bien parenthésée"""
    p = Pile()

    for c in ch:
        if c == "(":
            p.empiler(c)

        elif c == ")":
            if p.est_vide():
                return False
            else:
                p.depiler()

    return p.est_vide()


print(bon_parenthesage("((()())(()))"))  # True
print(bon_parenthesage("())(()"))  # False
print(bon_parenthesage("(())(()"))  # False
