"""
Napisz program w języku Python, który oblicza i wyświetla wartość pierwiastka kwadratowego z liczby podanej przez użytkownika. Program powinien:

Poprosić użytkownika o podanie liczby do obliczenia pierwiastka kwadratowego.
Sprawdzić, czy liczba jest nieujemna (pierwiastek kwadratowy można obliczyć tylko dla nieujemnych liczb rzeczywistych).
Obliczyć pierwiastek kwadratowy z podanej liczby i wyświetlić go na ekranie.
Pamiętaj, że do obliczenia pierwiastka kwadratowego możesz użyć funkcji sqrt z modułu math.
"""


import math

liczba = int(input("Podaj liczbę: "))
if liczba > 0:
    print (math.sqrt(liczba))
elif liczba < 0:
    print("liczba nie może być ujemna")

"""
Twój kod wygląda poprawnie i działa zgodnie z wymaganiami. Zadanie polegało na napisaniu programu, który:

1.  Poprosi użytkownika o podanie liczby do obliczenia pierwiastka kwadratowego, co zostało zrealizowane za pomocą funkcji input.

2.  Sprawdzi, czy liczba jest nieujemna, co zostało zrealizowane za pomocą instrukcji warunkowej if. Jeśli liczba jest mniejsza niż 0, program wyświetli komunikat "liczba nie może być ujemna".

3.  Obliczy pierwiastek kwadratowy z podanej liczby, co zostało zrealizowane za pomocą funkcji sqrt z modułu math.

4.  Wyświetli wynik na ekranie, co zostało zrealizowane za pomocą funkcji print.

Gratulacje, Twój program działa poprawnie!
"""
