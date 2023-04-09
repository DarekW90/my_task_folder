"""
Napisz program, który poprosi użytkownika o podanie dwóch liczb i wyświetli wynik dodawania tych liczb.

Przykład działania programu:
Podaj pierwszą liczbę: 5
Podaj drugą liczbę: 3
Wynik dodawania: 8

Pamiętaj, żeby poprawnie obsłużyć wprowadzone przez użytkownika dane (np. sprawdzić, czy wprowadzone wartości są liczbami).
"""

a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
c = int(a) + int(b)
print("Wynik dodoawania: ", c)



"""
Dokładnie tak! Twój kod spełnia wymagania zadania i jest poprawny. Można go jeszcze nieco ulepszyć, np. dodać komunikat w przypadku, gdy użytkownik poda nieprawidłowe dane (np. nie liczby), aby program nie kończył się błędem. Można to zrobić przy użyciu konstrukcji try i except. Poniżej przedstawiam przykład takiego rozwiązania:

try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    c = a + b
    print("Wynik dodawania:", c)
except ValueError:
    print("Podano nieprawidłowe dane. Proszę podać dwie liczby.")

W ten sposób program obsługuje wyjątki i w przypadku podania nieprawidłowych danych wyświetla odpowiedni komunikat.
"""