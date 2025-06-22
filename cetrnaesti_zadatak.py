# Statistička analiza teksta - 10 najčešćih riječi

from collections import Counter
import string

ime_fajla = "cetrnaesti_zadatak.txt"

try:
    with open(ime_fajla, "r", encoding="utf-8") as fajl:
        sadrzaj = fajl.read().lower()

        # Uklanjanje interpunkcijskih znakova
        for znak in string.punctuation:
            sadrzaj = sadrzaj.replace(znak, "")

        rijeci = sadrzaj.split()
        brojac = Counter(rijeci)

        print("10 najčešćih riječi:")
        for rijec, broj in brojac.most_common(10):
            print(f"{rijec}: {broj}")
except FileNotFoundError:
    print(f"Greška: Fajl '{ime_fajla}' ne postoji.")
except Exception as e:
    print(f"Greška prilikom obrade fajla: {e}")
