a1 = int(input("Length in centimeters: "))  # in cm: 46
b1 = int(input("Height in centimeters: "))  # in cm: 31
c1 = int(input("Width in centimeters: "))  # in cm: 34
m = int(input("Mass in kilogram: "))  # in kg: 10
a = a1/100
b = b1/100
c = c1/100
V = a*b*c
V1 = V*100
print("Volume of a cat:", round(V1), "m^3.")
p1 = m*V
p = p1*1000
print("Density of a cat:", round(p), "kg/m^3.")

# p=mV, where m - mass, V - volume
# V=abc, where a, b, c - cat sides