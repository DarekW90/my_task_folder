"""
Napisz program, który pobiera od użytkownika listę liczb całkowitych (oddzielone przecinkami lub spacjami) i wyświetla ich sumę oraz średnią arytmetyczną.

Wskazówka: Aby rozdzielić napis na elementy, które zostaną przekonwertowane na liczby całkowite, możesz użyć metody split. Np. elementy = napis.split(","). Następnie, aby przekonwertować każdy element na liczbę całkowitą, możesz użyć funkcji map oraz funkcji int. Np. liczby = list(map(int, elementy)).
"""


text = input("Podaj liczby oddzielone od siebie przecinkami: ")
elements = text.strip().split(",")

suma = 0

for x in elements:
    x = int(x)
    suma += x

length = len(elements)
print("Suma podanych liczb: ", suma)
print("Średnia podanych liczb: ", suma / length)


"""
Dobrze! Twój program pobiera listę liczb od użytkownika, sumuje je oraz oblicza średnią arytmetyczną. Zastosowałeś także pętlę for oraz funkcję len, co jest dobrą praktyką.

Gratulacje! Teraz możesz przejść do kolejnego zadania lub kontynuować pracę z aktualnym projektem.

"""