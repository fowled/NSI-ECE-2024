"""NOTE: Exercice 1"""


def delta(tab: list):
    resultat = [tab[0]]

    for i in range(1, len(tab)):
        resultat.append(tab[i] - tab[i - 1])

    return resultat


print(delta([1000, 800, 802, 1000, 1003]))  # [1000, -200, 2, 198, 3]
print(delta([42]))  # [42]


"""NOTE: Exercice 2"""


class Expr:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        return self.gauche is None and self.droite is None

    def infixe(self):
        s = ""

        if self.gauche is not None:
            s = "(" + s + self.gauche.infixe()

        s = s + str(self.valeur)

        if self.droite is not None:
            s = s + self.droite.infixe() + ")"

        return s


# (1+2)
a = Expr(Expr(None, 1, None), "+", Expr(None, 2, None))
print(a.infixe())

# ((1+2)*(3+4))
b = Expr(
    Expr(Expr(None, 1, None), "+", Expr(None, 2, None)),
    "*",
    Expr(Expr(None, 3, None), "+", Expr(None, 4, None)),
)
print(b.infixe())

# ((3*(8+7))-(2+1))
e = Expr(
    Expr(Expr(None, 3, None), "*", Expr(Expr(None, 8, None), "+", Expr(None, 7, None))),
    "-",
    Expr(Expr(None, 2, None), "+", Expr(None, 1, None)),
)
print(e.infixe())
