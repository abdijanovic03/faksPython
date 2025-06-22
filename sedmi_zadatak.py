# Program za provjeru da li je unesena riječ palindrom

rijec = input("Unesite riječ: ").lower()

# Obrnuti string
obrnuta_rijec = rijec[::-1]

if rijec == obrnuta_rijec:
    print(f"Riječ '{rijec}' je palindrom.")
else:
    print(f"Riječ '{rijec}' nije palindrom.")
 