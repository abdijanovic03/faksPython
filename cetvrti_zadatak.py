# Program za prebrojavanje praznih mjesta, brojeva, slova i specijalnih karaktera u unesenom tekstu

tekst = input("Unesite tekst: ")

broj_praznih = 0
broj_brojeva = 0
broj_slova = 0
broj_specijalnih = 0

for karakter in tekst:
    if karakter.isspace():
        broj_praznih += 1
    elif karakter.isdigit():
        broj_brojeva += 1
    elif karakter.isalpha():
        broj_slova += 1
    else:
        broj_specijalnih += 1

print(f"Prazna mjesta: {broj_praznih}")
print(f"Brojeva: {broj_brojeva}")
print(f"Slova: {broj_slova}")
print(f"Specijalnih karaktera: {broj_specijalnih}")
