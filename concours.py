karvas = int(input())
poids1 = int(input()) 
age1 = int(input())
corne1 = input()
garrot1 = input()


note1 = int(corne1) * int(garrot1) + int(poids1)


print(note1)


indices = [i for i, x in enumerate(liste_prix) if x == min(liste_prix)]


for i in range(nbmarchands):
    prix_galette = int(input())
    liste_prix.append(prix_galette)

for prix in liste_prix:
    if prix == prix:
        liste_prix.append(prix)


prix_mini = liste_prix.index(min(liste_prix))

indices = [i for i, x in enumerate(liste_prix) if x == min(liste_prix)]

indice_max = max(indices)
print(indice_max)