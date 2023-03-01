# przeczytaj trzy liczby
liczba1 = int(input("Wprowadź pierwszą liczbę: "))
liczba2 = int(input("Wprowadź drugą liczbę: "))
liczba3 = int(input("Wprowadź trzecią liczbę: "))

# tymczasowo zakladamy, ze pierwszy numer
# jest najwieksza
# sprawdzimy to wkrótce
najwieksza_liczba = liczba1

# sprawdzamy, czy druga liczba jest wieksza niz obecna najwieksza_liczba
# i uaktualniamy najwieksza_liczba jezeli zachodzi taka potrzeba
if liczba2 > najwieksza_liczba:
    najwieksza_liczba = liczba2

# sprawdzamy, czy trzecia liczba jest wieksza niz obecna najwieksza_liczba
# i uaktualniamy najwieksza_liczba jezeli zachodzi taka potrzeba
if liczba3 > najwieksza_liczba:
    najwieksza_liczba = liczba3

print("Największą liczbą jest: ", najwieksza_liczba)