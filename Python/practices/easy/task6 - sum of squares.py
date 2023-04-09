"""
Oto proste zadanie dla początkującego programisty Python:

Napisz program, który będzie pobierał od użytkownika liczbę całkowitą n i oblicza sumę kwadratów liczb od 0 do n. Wykorzystaj pętlę for i funkcję range().

Oto kilka wskazówek, które mogą pomóc Ci w napisaniu programu:

1.  Poproś użytkownika o podanie liczby całkowitej n za pomocą funkcji input().
2.  Zmiennej n przypisz wartość wprowadzoną przez użytkownika, ale pamiętaj, żeby skonwertować ją na liczbę całkowitą przy użyciu funkcji int().
3.  Utwórz zmienną suma i przypisz jej wartość początkową 0.
4.  Za pomocą pętli for i funkcji range() przejdź przez liczby od 0 do n (włącznie), a następnie dodaj ich kwadraty do zmiennej suma.
5.  Po zakończeniu pętli wyświetl użytkownikowi sumę kwadratów liczb od 0 do n.
Powodzenia!

"""

try:
    n = input("Podaj liczbę całkowitą: ")
    n = int(n)
    suma = 0

    #for i in range(suma, n+1): #poprawka, nie trzeba podawać początku zakresu ponieważ nie podając zawsze przyjmuje domyślnie wartość zero !
    
    for i in range(n+1):
        suma += i**2 
    
    print("Suma kwadratów wynosi: ", suma)


except ValueError:
    print("podano złą wartość!")

"""
Twój kod wygląda poprawnie i działa zgodnie z wymaganiami. Pętla for iteruje przez liczby od 0 do n (włącznie), a następnie dodaje ich kwadraty do zmiennej suma. Jeśli użytkownik wprowadzi wartość, która nie może zostać przekonwertowana na liczbę całkowitą, program wyświetli komunikat o błędzie.

Jedyne, co zauważyłem, to że wartość początkowa zmiennej i w pętli for powinna być 0, a nie suma, ponieważ suma na początku ma wartość 0 i w takim przypadku pętla by nie została wykonana w ogóle. W związku z tym, pętla powinna wyglądać tak:


for i in range(n+1):
    suma += i**2


Ale ogólnie rzecz biorąc, Twój kod wydaje się poprawny.
"""

# po poprawieniu 

"""
Dokładnie, teraz Twój kod jest poprawny. Zmieniłeś wartość początkową zmiennej i w pętli for na 0, co jest właściwe i pozwala na wykonanie pętli dla wszystkich wartości od 0 do n (włącznie).

Teraz, gdy użytkownik poda wartość niecałkowitą lub inną wartość, która nie może zostać przekonwertowana na liczbę całkowitą, program wyświetli komunikat o błędzie i nie będzie kontynuował dalszego wykonywania programu.

Gratuluję, Twój program działa poprawnie i wykonuje to, co powinien.
"""
