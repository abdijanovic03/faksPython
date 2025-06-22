# Pogađanje broja između 1 i 100

import random

tajni_broj = random.randint(1, 100)
broj_pokusaja = 0

print("Pogodite broj između 1 i 100.")

while True:
    try:
        unos = int(input("Unesite broj: "))
        broj_pokusaja += 1

        if unos < tajni_broj:
            print("Veće.")
        elif unos > tajni_broj:
            print("Manje.")
        else:
            print(f"Pogodili ste broj! Traženi broj je bio {tajni_broj}.")
            print(f"Broj pokušaja: {broj_pokusaja}")
            break
    except ValueError:
        print("Greška: Unesite cijeli broj.")
