age = int(input())
poids_bagages = int(input())
prix = 0

if age == 60:
    prix = 0
elif age < 10:
    prix = 5
elif 10 <= age < 60 and poids_bagages < 20 or age > 60 and poids_bagages < 20:
    prix = 30
elif 10 <= age < 60 and poids_bagages >= 20 or age > 60 and poids_bagages >= 20:
    prix = 40

print(prix)



