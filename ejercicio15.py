x = int(input("ingrse el valor de x: "))
y = int(input("ingrse el valor de y: "))
z = int(input("ingrse el valor de z: "))
aux = x
x = z
z = y
y = aux
print("valores rotados:",x,y,z)