# Program za izračunavanje faktorijela broja koristeći while petlju

try:
    broj = int(input("Unesite pozitivan cijeli broj: "))
    if broj < 0:
        print("Greška: Uneseni broj nije pozitivan.")
        exit()
except ValueError:
    print("Greška: Niste unijeli ispravan cijeli broj.")
    exit()

faktorijel = 1
i = 1

while i <= broj:
    faktorijel *= i
    i += 1

print(f"Faktorijel broja {broj} je: {faktorijel}")
