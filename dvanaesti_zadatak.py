# Program za unos, zapis i čitanje teksta iz fajla

ime_fajla = "dvanaesti_zadatak.txt"

try:
    # Unos više redova teksta od korisnika
    broj_linija = int(input("Koliko redova teksta želite unijeti? "))

    with open(ime_fajla, "w", encoding="utf-8") as fajl:
        for i in range(broj_linija):
            linija = input(f"Unesite red {i + 1}: ")
            fajl.write(linija + "\n")

    # Čitanje i ispis sadržaja fajla
    print("\nSadržaj fajla:")
    with open(ime_fajla, "r", encoding="utf-8") as fajl:
        sadrzaj = fajl.read()
        print(sadrzaj)

except ValueError:
    print("Greška: Potrebno je unijeti cijeli broj.")
except Exception as e:
    print(f"Greška pri radu sa fajlom: {e}")
