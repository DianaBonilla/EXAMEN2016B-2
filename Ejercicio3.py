print("Calculo del volumen de una piscina")
print("1. Piscina rectangular")
print("2. Picina elíptica")
print("3. Piscina circula")
opcion = int(input("Ingrese la opcion que desea: "))
pi=3.1416
if opcion == 1:
    a = float(input("Ingrese el valor del primer lado: "))
    b = float(input("Ingrese el valor del segundo lado: "))
    h = float(input("Ingrese el valor de la altura: "))
    volumen = a * b * h
    print("El volumen de la piscina rectangular es: ",volumen,"cm3")

elif opcion == 2:
    
    a=float(input("Ingrese el valor del largo del rectangulo: "))
    b=float(input("Ingrese el valor del ancho del rectangulo: "))
    c=float(input("Ingrese la altura del rectangulo: "))
    area=pi*4*b
    volumen=(((pi*a)/(2*b))/2)*c
    print("El volumen de la piscina eliptica es: ",volumen)

elif opcion == 3:
    r = float(input("Ingrese el valor del radio del circulo: "))
    area = pi * r**2
    h = float(input("Ingrese la altura del rectangulo: "))
    volumen = area * h
    print("El volumen de la piscina circular es: ",round(volumen,3))
