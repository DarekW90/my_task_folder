"""
Napisz program, który dla zadanej liczby całkowitej n wyświetli na ekranie jej wartość podniesioną do kwadratu.

Podpowiedź: Do podnoszenia liczby do kwadratu można użyć operatora **.
"""

try:
    n = int(input("Podaj liczbę która zostanie podniesiona do kwadratu: "))
    print ("Twoja liczba podniesiona do kwadratu to: ",n**2)

except ValueError:
    print ("Podano złą wartość")

"""
Dobrze wykonane! Twój kod poprawnie podnosi wprowadzoną liczbę do kwadratu. Pamiętaj, żeby stosować wyjątki jak w powyższym kodzie w celu uniknięcia błędów w przypadku niepoprawnych danych wejściowych.
"""