
h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

# wprowadź tutaj swój kod
x=((h*60+m)+d)/60
y=x*60%60

print(str(int(x%24)) + ":" + str(int(y)))

h = int(input("Czas rozpoczęcia (godziny): "))
m = int(input("Czas rozpoczęcia (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))
m = m + d # oblicz ogólną liczbę minut
h = h + m // 60 # znajdź liczbę godzin ukrytych w minutach i zaktualizuj godzinę
m = m % 60 # prawidłowe minuty w zakresie (0..59)
h = h % 24 # prawidłowe godziny w zakresie (0..23)
print(h, ":", m, sep='')