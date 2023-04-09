"""
Oto kolejne zadanie, które również dotyczy operacji matematycznych:

Napisz program, który poprosi użytkownika o podanie dwóch liczb i wyświetli wynik mnożenia tych liczb.

Przykład działania programu:
Podaj pierwszą liczbę: 4
Podaj drugą liczbę: 7
Wynik mnożenia: 28

Pamiętaj, żeby poprawnie obsłużyć wprowadzone przez użytkownika dane (np. sprawdzić, czy wprowadzone wartości są liczbami).
"""

try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    c = a * b
    print("wynik mnożenia: ", c)
except ValueError:
    print("Podano złe dane, podaj dwie liczby")

'''
try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    c = a * b
    print("Wynik mnożenia:", c)
except ValueError:
    print("Podane wartości nie są liczbami.")
'''