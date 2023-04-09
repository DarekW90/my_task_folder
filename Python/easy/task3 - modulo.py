"""
Oto zadanie dla początkującego programisty Python:

Napisz program w Pythonie, który prosi użytkownika o wprowadzenie liczby całkowitej i sprawdza, czy wprowadzona liczba jest parzysta czy nieparzysta. Jeśli liczba jest parzysta, program powinien wyświetlić odpowiedni komunikat, informujący użytkownika o tym fakcie, a jeśli liczba jest nieparzysta, program powinien również wyświetlić odpowiedni komunikat.

Możesz użyć poniższego szablonu kodu, aby rozpocząć pracę:

python

liczba = int(input("Wprowadź liczbę: "))

if liczba % 2 == 0:
    print("Liczba", liczba, "jest parzysta")
else:
    print("Liczba", liczba, "jest nieparzysta")

Przykładowy wynik działania programu:

Wprowadź liczbę: 13
Liczba 13 jest nieparzysta

W tym zadaniu uczysz się podstawowej składni języka Python, pobierania danych od użytkownika, instrukcji warunkowych i operacji modulo. Powodzenia w nauce!

"""

try:
    liczba = int(input("Wprowadź liczbę: "))

    if liczba % 2 == 0:
        print("Liczba", liczba, "jest parzysta")
    else:
        print("Liczba", liczba, "jest nieparzysta")
        
except ValueError:
    print ("Podano, niepoprawne dane")
