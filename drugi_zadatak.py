# Program koji provjerava da li je uneseni broj paran ili neparan

# Pokušaj unosa cijelog broja
try:
    broj = int(input("Unesite cijeli broj: "))
except ValueError:
    print("Greška: Niste unijeli ispravan cijeli broj.")
    exit()

# Provjera da li je broj paran ili neparan
if broj % 2 == 0:
    print(f"Broj {broj} je paran.")
else:
    print(f"Broj {broj} je neparan.")
