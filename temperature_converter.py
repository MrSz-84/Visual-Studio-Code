# Variables input
celsius = float(input("Input temperature in Centigrade: " ))
fahrenheit = float(input("Input temperature in Fahrenheit scale: "))
kelvin = float(input("Enter temperature in Kelvin scale: "))

# Conversion calculations
celsius_to_fahrenheit = ((celsius * (9/5)) + 32)
fahrenheit_to_celsius = ((fahrenheit - 32) * (5/9))
celsius_to_kelvin = (celsius + 273.15)
kelvin_to_celsius = (kelvin - 273.15)
kelvin_to_fahrenheit = (((kelvin - 273.15) * 1.8) + 32)
fahrenheit_to_kelvin = ((fahrenheit + 459.67) * (5/9))

# Output data
print("MrSz Corporation ©, Wroclaw 2023.", "All rights reserved. \n")
print(celsius, "'C is:", round(celsius_to_fahrenheit, 1), "'F")
print(fahrenheit, "'F is:", round(fahrenheit_to_celsius, 1), "'C")
print(celsius, "'C is:", round(celsius_to_kelvin, 1), "'K")
print(kelvin, "'K is:", round(kelvin_to_celsius, 1), "'C")
print(kelvin, "'K is:", round(kelvin_to_fahrenheit, 2), "'F")
print(fahrenheit, "'F is:", round(fahrenheit_to_kelvin, 2), "'K")