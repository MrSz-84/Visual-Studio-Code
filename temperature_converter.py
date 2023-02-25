celsius = 32.4
fahrenheit = 68.9
kelvin = 298.6

celsius_to_fahrenheit = ((celsius * (9/5)) + 32)
fahrenheit_to_celsius = ((fahrenheit - 32) * (5/9))
celsius_to_kelvin = celsius + 273.15
kelvin_to_celsius = kelvin - 273.15

print("MrSz Corporation ©, Wroclaw 2023.", "All rights reserved. \n")
print(celsius, "'C is", round(celsius_to_fahrenheit, 1), "'F")
print(fahrenheit, "'F is", round(fahrenheit_to_celsius, 1), "'C")
print(celsius, "'C is", round(celsius_to_kelvin, 1), "'K")
print(kelvin, "'K is", round(kelvin_to_celsius, 1), "'C")