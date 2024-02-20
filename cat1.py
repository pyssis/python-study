a = int(input("Length: ")) #in cm: 46
b = int(input("Height: ")) #in cm: 31
c = int(input("Width: ")) #in cm: 34
m = int(input("Mass: ")) #in gramm: 10 000
V = a*b*c
print("Volume of a cat:", V, "cm^3.")
p = m*V
print("Density of a cat:", p, "g/cm^3.")

# p=mV, where m - mass, V - volume
# V=abc, where a, b, c - cat sides
