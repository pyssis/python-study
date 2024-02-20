a = int(input("Length in centimeters: "))  # in cm: 46
b = int(input("Height in centimeters: "))  # in cm: 31
c = int(input("Width in centimeters: "))  # in cm: 34
m = int(input("Mass in kilogram: "))  # in kg: 10
V = a*b*c
print("Volume of a cat:", V, "cm^3.")
M = m*1000  #kg in g
p = M/V
print("Density of a cat: ", p, " g/cm^3.")

# p=m/V, where m - mass, V - volume
# V=abc, where a, b, c - cat sides