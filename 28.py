"""NOTE: Exercice 1"""


def fibonacci(n: int):
    suite = [1, 1]

    if n == 1 or n == 2:
        return 1

    while len(suite) < n:
        somme = suite[-1] + suite[-2]
        suite.append(somme)

    return suite[-1]


print(fibonacci(1))  # 1
print(fibonacci(2))  # 1
print(fibonacci(25))  # 75025


"""NOTE: Exercice 2"""


def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []

    for i in range(len(notes)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])

        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi, meilleurs_eleves)


eleves_nsi = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]

print(eleves_du_mois(eleves_nsi, notes_nsi))  # (80, ['c', 'f', 'h'])
print(eleves_du_mois([], []))  # (0, [])
