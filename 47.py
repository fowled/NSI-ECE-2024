"""NOTE: Exercice 1"""


def max_dico(dico: dict):
    maxi = None

    for valeur in dico:
        if maxi == None or dico[valeur] > maxi[1]:
            maxi = (valeur, dico[valeur])

    return maxi


# ('Ada', 201)
print(max_dico({"Bob": 102, "Ada": 201, "Alice": 103, "Tim": 50}))

# ('Alan', 222)
print(max_dico({"Alan": 222, "Ada": 201, "Eve": 222, "Tim": 50}))


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


def eval_expression(tab):
    p = Pile()

    for element in tab:
        if element != "+" and element != "*":
            p.empiler(element)
        else:
            if element == "+":
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()

            p.empiler(resultat)

    return p.depiler()


print(eval_expression([2, 3, "+", 5, "*"]))  # 25
print(eval_expression([1, 2, "+", 3, "*"]))  # 9
print(eval_expression([1, 2, 3, "+", "*"]))  # 5
