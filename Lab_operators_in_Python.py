x = float(input("Wprowadź wartość dla x: "))

y = 1/(x+(1/(x+(1/(x+(1/x))))))

print("y =", y)

print("\n")
print("\n")

x = float(input("Wprowadź wartość dla x: "))
a = (x + (1/x))
b = (x + (1/(a)))
c = (x + (1/(b)))

y = 1/c
print("y =", y)