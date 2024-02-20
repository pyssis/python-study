a = int(input("Length in centimeters: "))  # in cm: 46
b = int(input("Height in centimeters: "))  # in cm: 31
c = int(input("Width in centimeters: "))  # in cm: 34
V = a*b*c
print("Volume of a cat:", round(V), "cm^3.")
p = 19.05  # g/cm^3
m = V*p
M = m*0.001
print("Mass of a cat:", round(M), "kg.")

# m=pV