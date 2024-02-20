a1 = int(input("Length in centimeters: "))  # in cm: 46
b1 = int(input("Height in centimeters: "))  # in cm: 31
c1 = int(input("Width in centimeters: "))  # in cm: 34
a = a1/100
b = b1/100
c = c1/100
V1 = a*b*c
V = V1*100
print("Volume of a cat:", round(V), "m^3.")
UranP = 19.05  # g/cm^3
p = UranP*1000
m = V*p
print("Mass of a cat:", round(m), "kg.")
