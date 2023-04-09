"""
Napisz program w języku Python, który:

1.  Poprosi użytkownika o wprowadzenie dowolnego napisu (np. zdania).
2.  Sprawdzi, czy podany napis jest palindromem (tzn. czy czytany od lewej do prawej i od prawej do lewej daje ten sam wynik).
3.  Wyświetli informację na temat tego, czy podany napis jest palindromem.

Pamiętaj, żeby zignorować spacje i inne znaki specjalne podczas sprawdzania, czy napis jest palindromem.

"""
#dodatkowe wskazówki
"""
1.  Użyj funkcji input, aby poprosić użytkownika o wprowadzenie napisu. Np. napis = input("Podaj napis: ").
2.  Aby sprawdzić, czy napis jest palindromem, możesz porównać napis z jego odwróconą wersją. Możesz odwrócić napis za pomocą operatora slicingu [start:stop:step]. Np. odwrocony_napis = napis[::-1].
3.  Przed porównaniem napisu i jego odwróconej wersji, usuń spacje i znaki specjalne z obu napisów za pomocą metody replace. Np. napis = napis.replace(" ", "").replace(",", "").replace(".", "").
4.  Porównaj napis i jego odwróconą wersję za pomocą instrukcji warunkowej if.

Pamiętaj, żeby stworzyć program w sposób uniwersalny, który będzie działał dla różnych długości napisów i różnych kombinacji znaków.
"""

napis = input("Podaj napis: ")

# Usuń spacje i znaki specjalne z napisu
napis = napis.replace(" ", "").replace(",", "").replace(".", "")

# Odwróć napis
odwrocony_napis = napis[::-1]

# Sprawdź, czy napis jest palindromem
if napis == odwrocony_napis:
    print("Podany napis jest palindromem.")
else:
    print("Podany napis nie jest palindromem.")

"""    
Program pobiera napis od użytkownika, usuwa spacje i znaki specjalne z napisu, odwraca napis i sprawdza, czy napis i jego odwrócona wersja są sobie równe. Jeśli tak, to program wyświetla komunikat "Podany napis jest palindromem", a w przeciwnym przypadku wyświetla komunikat "Podany napis nie jest palindromem".

"""