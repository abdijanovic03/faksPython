# Program za izračunavanje prosječne ocjene studenta

try:
    broj_ocjena = int(input("Unesite broj ocjena: "))
    if broj_ocjena <= 0:
        print("Greška: Broj ocjena mora biti pozitivan.")
        exit()
except ValueError:
    print("Greška: Niste unijeli ispravan broj ocjena.")
    exit()

suma = 0.0

for i in range(broj_ocjena):
    try:
        ocjena = float(input(f"Unesite ocjenu #{i+1}: "))
    except ValueError:
        print("Greška: Niste unijeli validnu ocjenu.")
        exit()
    suma += ocjena

prosjek = suma / broj_ocjena
print(f"Prosječna ocjena je: {prosjek:.2f}")
