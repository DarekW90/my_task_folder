"""
Oto zadanie: Napisz program, który oblicza pole powierzchni i objętość stożka, dla podanych długości promienia podstawy (r) i wysokości (h) stożka. Wyniki powinny być wyświetlone z dokładnością do dwóch miejsc po przecinku.

Podpowiedź: Do obliczenia pola i objętości stożka wykorzystaj wzory matematyczne.
"""
import math

try: 
    r = float(input("Podaj długość promienia podstawy stożka: "))
    h = float(input("Podaj wysokość stożka: "))

    #pole powierzchni Pp = Pi*r^2
    Pp = math.pi * r**2
    #objętość V = 1/3 Pp * h
    V = (1/3 * Pp) * h 

    print ("Pole powierzchni danego stożka to: ", Pp)
    print ("Objętość tego stożka to: ", V)


except ValueError:
    print("Podano złą wartość")

"""
Zadanie to obliczenie pola powierzchni oraz objętości stożka na podstawie długości promienia podstawy oraz wysokości. W tym celu użyto biblioteki math oraz podano wartości długości promienia i wysokości ze strony użytkownika.

W pierwszej kolejności obliczono pole powierzchni koła o promieniu r, czyli Pp = pi*r^2. Następnie obliczono objętość stożka V = 1/3 Pp * h, gdzie h to podana przez użytkownika wysokość stożka.

Wyniki zostały wypisane na ekranie wraz z odpowiednim komunikatem dla użytkownika.
"""