print("Calculo del volumen de una piscina")
print("1. Piscina rectangular")
print("2. Picina elíptica")
print("3. Piscina circula")
opcion = int(input("Ingrese la opcion que desea: "))
if opcion == 1:
    a = float(input("Ingrese el valor del primer lado: "))
    b = float(input("Ingrese el valor del segundo lado: "))
    h = float(input("Ingrese el valor de la altura: "))
    volumen = a * b * h
    print("El volumen de la piscina rectangular es: ",volumen,"cm3")
