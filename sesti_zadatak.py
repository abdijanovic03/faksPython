# Program za brojanje samoglasnika u unesenoj rečenici

rečenica = input("Unesite rečenicu: ")

samoglasnici = "aeiou"
broj_samoglasnika = 0

for karakter in rečenica.lower():
    if karakter in samoglasnici:
        broj_samoglasnika += 1

print(f"Ukupno samoglasnika u rečenici je: {broj_samoglasnika}")
