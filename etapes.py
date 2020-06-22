jours_de_marche = int(input())
nbres_kms = 0
etapes = []  # 36 14 38 28 29 31

print()
for i in range(jours_de_marche):
    nbres_kms = int(input())
    etapes.append(nbres_kms)

plus_longue_etape = max(etapes)
print()
print(plus_longue_etape)

