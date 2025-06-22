# Program za dijeljenje dva broja uz provjeru da se ne dijeli nulom

# Pokušaj unosa prvog broja (djeljenik)
try:
    djeljenik = float(input("Unesite prvi broj (djeljenik): "))
except ValueError:
    print("Greška: Niste unijeli ispravan broj.")
    exit()

# Petlja za unos drugog broja (djelilac), sa provjerom da nije nula
while True:
    try:
        djelilac = float(input("Unesite drugi broj (djelilac): "))
        if djelilac == 0:
            print("Greška: Nije dozvoljeno dijeljenje s nulom. Pokušajte ponovo.")
        else:
            break  # Ispravan unos, izlazimo iz petlje
    except ValueError:
        print("Greška: Niste unijeli broj. Pokušajte ponovo.")

# Računanje i ispis rezultata
rezultat = djeljenik / djelilac
print(f"Rezultat dijeljenja broja {djeljenik} sa {djelilac} je: {round(rezultat,2)}")

