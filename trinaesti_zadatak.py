# Program za brojanje riječi u fajlu "tekst.txt"

ime_fajla = "trinaesti_zadatak.txt"

try:
    with open(ime_fajla, "r", encoding="utf-8") as fajl:
        sadrzaj = fajl.read()
        rijeci = sadrzaj.split()
        broj_rijeci = len(rijeci)
        print(f"Ukupan broj riječi u fajlu je: {broj_rijeci}")
except FileNotFoundError:
    print(f"Greška: Fajl '{ime_fajla}' ne postoji.")
except Exception as e:
    print(f"Greška prilikom čitanja fajla: {e}")
