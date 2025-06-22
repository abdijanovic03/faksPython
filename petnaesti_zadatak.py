import re

# Validacija imena
def validiraj_ime(ime):
    return bool(re.fullmatch(r"[A-Za-zĆČŽŠĐćčžšđ ]{3,}", ime)) and len(ime.split()) >= 2

# Validacija e-mail adrese
def validiraj_email(email):
    return re.fullmatch(r".+@.+\.(com|ba|org|edu)", email) is not None

# Validacija lozinke
def validiraj_lozinku(lozinka):
    if len(lozinka) < 8:
        return False
    if not re.search(r"[A-Z]", lozinka):
        return False
    if not re.search(r"[a-z]", lozinka):
        return False
    if not re.search(r"[0-9]", lozinka):
        return False
    if not re.search(r"[^\w\s]", lozinka):  # Specijalni znak
        return False
    return True

# Unos i provjera
ime = input("Unesite ime i prezime: ")
email = input("Unesite e-mail adresu: ")
lozinka = input("Unesite lozinku: ")

if not validiraj_ime(ime):
    print("Greška: Ime mora sadržavati samo slova i imati bar dvije riječi.")
elif not validiraj_email(email):
    print("Greška: E-mail adresa nije validna.")
elif not validiraj_lozinku(lozinka):
    print("Greška: Lozinka mora imati najmanje 8 znakova, veliko slovo, malo slovo, broj i specijalni znak.")
else:
    print("Uspješna registracija!")
