# Program za brojanje pojavljivanja svakog karaktera u unesenom stringu

# Unos stringa od korisnika
tekst = input("Unesite tekst: ")

# Objekt za čuvanje broja pojavljivanja karaktera
brojac = {}

# Prolazak kroz svaki karakter u stringu
for karakter in tekst:
    if karakter in brojac:
        brojac[karakter] += 1  # povećavamo broj za 1 ako karakter već postoji
    else:
        brojac[karakter] = 1   # prvi put se pojavljuje karakter

# Ispis rezultata
print("Broj pojavljivanja svakog karaktera:")
for karakter, broj in brojac.items():
    print(f"'{karakter}': {broj}")
