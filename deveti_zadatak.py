# Program za generisanje prvih n članova Fibonačijevog niza

try:
    n = int(input("Unesite koliko članova Fibonačijevog niza želite: "))
    if n <= 0:
        print("Greška: Broj mora biti pozitivan.")
        exit()
except ValueError:
    print("Greška: Niste unijeli ispravan cijeli broj.")
    exit()

a, b = 0, 1
fibonacci = []

for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b

print("Fibonačijev niz:", *fibonacci)
