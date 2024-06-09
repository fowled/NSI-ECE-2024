"""NOTE: Exercice 1"""


def correspond(mot: str, mot_a_trous: str):
    if len(mot_a_trous) != len(mot):
        return False

    for i in range(len(mot)):
        if mot_a_trous[i] != mot[i] and mot_a_trous[i] != "*":
            return False

    return True


print(correspond("INFORMATIQUE", "INFO*MA*IQUE"))  # True
print(correspond("AUTOMATIQUE", "INFO*MA*IQUE"))  # False
print(correspond("STOP", "S*"))  # False
print(correspond("AUTO", "*UT*"))  # True


"""NOTE: Exercice 2"""


def est_cyclique(plan):
    expediteur = "A"
    destinataire = plan[expediteur]
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires += 1

    return nb_destinataires == len(plan)


# False
print(est_cyclique({"A": "E", "F": "A", "C": "D", "E": "B", "B": "F", "D": "C"}))

# True
print(est_cyclique({"A": "E", "F": "C", "C": "D", "E": "B", "B": "F", "D": "A"}))

# True
print(est_cyclique({"A": "B", "F": "C", "C": "D", "E": "A", "B": "F", "D": "E"}))

# False
print(est_cyclique({"A": "B", "F": "A", "C": "D", "E": "C", "B": "F", "D": "E"}))
