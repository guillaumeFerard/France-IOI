nbre_maisons = int(input())
abscisses = []
ordonnees = []
longueur_abscisse = 0
longueur_ordonnee = 0


for i in range(nbre_maisons):
    x = int(input())
    y = int(input())
    abscisses.append(x)
    ordonnees.append(y)

longueur_abscisse = max(abscisses) - min(abscisses)
longueur_ordonnee = max(ordonnees) - min(ordonnees)
perimetre = (longueur_abscisse + longueur_ordonnee) * 2
print()
print(perimetre)

# 4 1 5 5 3 4 6 2 9

