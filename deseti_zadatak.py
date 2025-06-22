# Kalkulator 

while True:
    print("\nIzaberite operaciju:")
    print("1. Sabiranje")
    print("2. Oduzimanje")
    print("3. Množenje")
    print("4. Dijeljenje")
    print("5. Izlaz")

    izbor = input("Unesite opciju (1-5): ")

    if izbor == '5':
        print("Izlaz iz programa.")
        break

    if izbor not in ['1', '2', '3', '4']:
        print("Neispravan izbor, pokušajte ponovo.")
        continue

    try:
        broj1 = float(input("Unesite prvi broj: "))
        broj2 = float(input("Unesite drugi broj: "))
    except ValueError:
        print("Greška: Morate unijeti validne brojeve.")
        continue

    if izbor == '1':
        rezultat = broj1 + broj2
        print(f"Rezultat sabiranja: {rezultat}")
    elif izbor == '2':
        rezultat = broj1 - broj2
        print(f"Rezultat oduzimanja: {rezultat}")
    elif izbor == '3':
        rezultat = broj1 * broj2
        print(f"Rezultat množenja: {rezultat}")
    elif izbor == '4':
        if broj2 == 0:
            print("Greška: Dijeljenje sa nulom nije dozvoljeno.")
            continue
        rezultat = broj1 / broj2
        print(f"Rezultat dijeljenja: {rezultat}")
