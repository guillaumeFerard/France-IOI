nbjetons = int(input())

for i in range(nbjetons):
    x = int(input())
    y = int(input())

    if 0 < x < 90 or 0 < y < 70:
        if 10 < x < 85 and 10 < y < 55 and not (25 < x < 50 and 20 < y < 45):
            print("Dans une zone bleue")
        elif 15 < x < 45 or 60 < x < 85 and y > 60:
            print("Dans une zone rouge")
        else:
            print("Dans une zone jaune")
    else:
        print("En dehors de la feuille")
