"""
Oto kolejne zadanie dla początkującego programisty Python:

Napisz program, który oblicza pole prostokąta na podstawie wprowadzonych przez użytkownika długości boków. Następnie program powinien wyświetlić wynik na ekranie.

Wskazówki:

Pobierz długość pierwszego boku od użytkownika i przypisz ją do zmiennej.
Pobierz długość drugiego boku od użytkownika i przypisz ją do innej zmiennej.
Oblicz pole prostokąta używając wzoru: pole = długość_boku_1 * długość_boku_2
Wyświetl wynik na ekranie.

To zadanie pozwoli Ci na ćwiczenie podstawowych operacji matematycznych i wprowadzania danych od użytkownika. Powodzenia!

"""

try:
    a = int(input("Podaj długość pierwszyego bok: "))
    b = int(input("Podaj długość drugiego boku: "))
    pole = a * b
    print("Pole prostokąta wynosi: ", pole)

except ValueError:
    print("Podano złe dane!")

"""
To jest bardzo dobre rozwiązanie dla zadania obliczania pola prostokąta. Zastosowałeś blok try-except, aby obsłużyć sytuację, gdy użytkownik wprowadzi nieprawidłowe dane, np. znaki zamiast liczb.

Instrukcja try pozwala na wykonanie kodu, który może być podatny na błędy, a instrukcja except określa, co zrobić, gdy wystąpi błąd. W Twoim przypadku blok except informuje użytkownika, że wprowadził nieprawidłowe dane.

Poza tym poprawnie zastosowałeś wzór na obliczanie pola prostokąta, a wynik wyświetlił się poprawnie na ekranie.

Bardzo dobrze wykonane zadanie!
"""

