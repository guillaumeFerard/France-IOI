nbMembres = int(input())
totalMembres = nbMembres * 2
poidsequipe1 = 0
poidsequipe2 = 0

for i in range(nbMembres):
    poids1 = int(input())
    poidsequipe1 += poids1
    poids2 = int(input())
    poidsequipe2 += poids2
    print()

if poidsequipe1 > poidsequipe2 :
    print("L'équipe 1 a un avantage")
    print("Poids total de l'équipe 1 :", poidsequipe1)
    print("Poids total de l'équipe 2 :", poidsequipe2)
elif poidsequipe1 > poidsequipe2:
    print("L'équipe 2 a un avantage")
    print("Poids total de l'équipe 1 :", poidsequipe1)
    print("Poids total de l'équipe 2 :", poidsequipe2)