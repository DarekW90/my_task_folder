"""
Napisz program, który poprosi użytkownika o podanie dwóch liczb całkowitych a i b, a następnie wyświetli wynik ich dodawania, odejmowania, mnożenia i dzielenia.

Podpowiedź: Pamiętaj o sprawdzeniu poprawności wprowadzonych danych, tak aby program działał poprawnie dla liczb całkowitych.
"""
try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

    print()
    print ("Wynik dodawania podanych liczb to: ", a+b)
    print ("Wynik odejmowania podanych liczb to: ", a-b)
    print ("Wynik mnożenia podanych liczb to: ", a*b)
    print ("Wynik dzielenia podanych liczb to: ", a/b)
    print()


except ValueError:
    print ("Podano złą wartość")