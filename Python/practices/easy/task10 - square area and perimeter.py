"""
Napisz program w Pythonie, który przyjmuje długość boku kwadratu od użytkownika, a następnie oblicza i wyświetla pole oraz obwód tego kwadratu.
"""

try:
    lenght = int(input("Podaj długość boku kwadratu: "))
    print("Pole kwadratu wynosi: ", lenght**2)
    print("Obwód kwadratu wynosi: ", lenght*4)
except ValueError:
    print("Podano złą wartości")


"""
Dobrze! Twój program poprawnie oblicza pole i obwód kwadratu. Użyłeś do tego prostych działań arytmetycznych, co jest dobrym rozwiązaniem w przypadku tak prostego zadania.

Pamiętaj jednak o formatowaniu wyjścia, aby prezentować wyniki w czytelny i estetyczny sposób. Można to zrobić np. za pomocą metody .format() lub operatora %.

Gratulacje! Teraz możesz przejść do kolejnego zadania lub kontynuować pracę z aktualnym projektem.



Oto dwa inne sposoby prezentacji wyników:

            Metoda .format()

lenght = int(input("Podaj długość boku kwadratu: "))
pole = lenght ** 2
obwod = 4 * lenght

print("Pole kwadratu wynosi: {:.2f}".format(pole))
print("Obwód kwadratu wynosi: {:.2f}".format(obwod))

W tym przypadku użyliśmy metody .format() do sformatowania wyników i ograniczenia ich do dwóch miejsc po przecinku.

            Operator %

lenght = int(input("Podaj długość boku kwadratu: "))
pole = lenght ** 2
obwod = 4 * lenght

print("Pole kwadratu wynosi: %.2f" % pole)
print("Obwód kwadratu wynosi: %.2f" % obwod)

W tym przypadku użyliśmy operatora % do sformatowania wyników i ograniczenia ich do dwóch miejsc po przecinku.
"""