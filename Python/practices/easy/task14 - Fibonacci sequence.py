"""
Napisz program, który obliczy n-ty wyraz ciągu Fibonacciego. Ciąg Fibonacciego to ciąg liczb, w którym pierwsze dwa wyrazy wynoszą kolejno 0 i 1, a każdy następny wyraz jest sumą dwóch poprzednich.

Przykładowo, piąty wyraz ciągu Fibonacciego wynosi 5, ponieważ 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5.

Podpowiedź: Można rozwiązać to zadanie przy użyciu pętli for lub rekurencyjnie.
"""


n = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))

# Pierwsze dwa wyrazy ciągu to 0 i 1
fib = [0, 1]

# Obliczamy n-ty wyraz ciągu Fibonacciego
for i in range(2, n+1):
    fib.append(fib[i-1] + fib[i-2])

print(f"n-ty wyraz ciągu Fibonacciego wynosi: {fib[n]}")


# odpowiedz wygenerowana przez chat