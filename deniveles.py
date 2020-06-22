nbre = int(input())   # 5 4 7 -6 -3 2
montees = []
descentes = []

print()

for i in range(nbre):
    denivele = int(input())
    if denivele > 0:
        montees.append(denivele) 
    
    if denivele < 0:
        denivele = denivele * -1
        descentes.append(denivele)
   

print()
print(sum(montees))
print(sum(descentes))