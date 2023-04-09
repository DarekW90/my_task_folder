"""
Oto kolejne zadanie dla początkującego programisty Python:

Napisz program, który pozwoli użytkownikowi wprowadzić ciąg liczb oddzielonych przecinkami, a następnie wyświetli na ekranie sumę tych liczb.

Wskazówki:

Pobierz ciąg liczb oddzielonych przecinkami od użytkownika i przypisz go do zmiennej.
Wykorzystaj metodę split() do podzielenia ciągu na pojedyncze liczby.
Skonwertuj każdą z tych liczb na typ float i dodaj je do siebie, aby obliczyć sumę.
Wyświetl wynik na ekranie.

To zadanie pozwoli Ci na ćwiczenie manipulowania ciągami znaków, konwersji typów i podstawowych operacji matematycznych. Powodzenia!
"""


"""
Oczywiście, chętnie udzielę Ci dodatkowych wskazówek dotyczących tego zadania.

    Po pobraniu ciągu znaków od użytkownika, możesz usunąć spacje przy pomocy metody strip(), aby uniknąć problemów z parsowaniem liczb.

    Metoda split() pozwoli Ci na podzielenie ciągu znaków na pojedyncze liczby oddzielone przecinkami. Dzięki temu będziesz mógł przetworzyć każdą z liczb osobno.

    Aby zamienić ciąg znaków na liczbę, możesz skorzystać z funkcji float() lub int(). Pamiętaj, że metoda split() zwraca listę ciągów znaków, dlatego musisz wywołać tę funkcję dla każdej liczby osobno.

    Po przetworzeniu wszystkich liczb, musisz je dodać, aby uzyskać ich sumę. W tym celu możesz skorzystać z pętli for, która pozwoli Ci przejść przez wszystkie liczby na liście.

    Na końcu wyświetl wynik za pomocą funkcji print(). Pamiętaj, aby zamienić sumę na ciąg znaków, przed wyświetleniem jej na ekranie.

Mam nadzieję, że te wskazówki pomogą Ci w rozwiązaniu tego zadania."""

"""
data = input("Podaj serie liczb oddzielone przecinkami: ")
x = data.split()
print(x)
"""

# pobieramy ciąg liczb oddzielonych przecinkami od użytkownika
ciag = input("Podaj ciąg liczb oddzielonych przecinkami: ")

# dzielimy ciąg na pojedyncze liczby
liczby = ciag.strip().split(",")

# inicjalizujemy zmienną przechowującą sumę
suma = 0

# przetwarzamy każdą z liczb
for liczba in liczby:
    # konwertujemy ciąg znaków na liczbę typu float
    liczba = float(liczba)
    # dodajemy liczbę do sumy
    suma += liczba

# wyświetlamy wynik
print("Suma podanych liczb wynosi:", suma)
