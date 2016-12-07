#ESCUELA POLITECNICA NACIONAL

from time import*
import os

def creartxt_ejercicio2():
    archi=open("Numero_Repeticiones.txt",'w')
    archi.close()

def leertxt_ejercicio2():
    tiempo=0
##    repeticion=0
    nombre='Jordan'
    archi=open('nombres1024KB.txt','r')
    inicio=time()
##    linea=archi.readline()
##    cadena=linea.split(' ')
##    palabras=len(cadena)
##    for i in range(palabras):
##        if palabras[i]==nombre:
##            repeticion=repeticion+1
##    while linea != "":
##        linea=archi.readline()
##        cadena=linea.split(' ')
##        palabras=len(palabras)
##        for i in range(palabras):
##            if palabras[i]==nombre:
##                repeticion=repet
##                icion+1
##    fin=time()
##    archi.close()
    cont=0
    numero=0
##    archi=open(archivo,'r')
    linea=archi.readline()
    #print(linea.count(palabra))
    while linea !="":
        cont+=linea.count(nombre)
        #print (linea)
        linea=archi.readline()
    numero=cont
    print("La palabra ingresada: ",nombre," se repite: ",numero," veces en el texto")
    fin=time()
##    archi.close()
    tiempo=fin-inicio
    archi=open('Numero_Repeticiones.txt','a')
    archi.write('El numero de repeticiones es: '+ str(numero))
    archi.write('\nEl tiempo transcurrido fue: '+ str(tiempo))
    archi.close()

def ejercicio1():
    def crear():
        a=open('nombre.txt','w')
        a=open('nombre.txt','a')
        a1=open('nombres1024KB.txt','w')
        a.write('Bonilla Valdivieso Diana Estefania \n')
        a.write('Carrillo Morocho Jessica Vanessa \n')
        a.write('Osorio Gonzalez Edison Santiago \n')
        a.write('Sanchez Hernandez Jordan Sebastian \n')
        a.write('Hernandez Alamgro Edison David \n')
        a.close()
        a1.close()

    def repetir100():
        a=open('nombre.txt','w')
        for i in range(600):
            a.write('Bonilla Valdivieso Diana Estefania\n')
            a.write('Carrillo Morocho Jessica Vanessa\n')
            a.write('Hernandez Almagro Edison David\n')
            a.write('Osorio Gonzales Edison Santiago\n')
            a.write('Sanchez Hernandez Jordan Sebastian\n')
        a.close()
    
    def repetir1024():
        a1=open('nombres.txt','w')
        a1=open('nombres1024KB.txt','a')
        for i in range(6189):
            a1.write('Bonilla Valdivieso Diana Estefania\n')
            a1.write('Carrillo Morocho Jessica Vanessa\n')
            a1.write('Hernandez Almagro Edison David\n')
            a1.write('Osorio Gonzales Edison Santiago\n')
            a1.write('Sanchez Hernandez Jordan Sebastian\n')
        a1.close()

    def leer():
        a1=open('nombre.txt','r')
        linea=a1.readline()
        while linea !='':
            print(linea)
            linea=a1.readline()
        a1.close()
    print("")

##    def main():
    crear()
    repetir100()
    repetir1024()
    leer()

def ejercicio2():
    print("\tEjercicio 2")
    creartxt_ejercicio2()
    leertxt_ejercicio2()

def ejercicio3():
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
        a=float(input("Ingrese el valor semieje MAYOR: "))
        b=float(input("Ingrese el valor del semieje MENOR: "))
        c=float(input("Ingrese la altura del rectangulo: "))
        area=pi*a*b
        volumen=area*c
        print("El volumen de la piscina eliptica es: ",round(volumen,2),"cm3")
    elif opcion == 3:
        r = float(input("Ingrese el valor del radio del circulo: "))
        area = pi * r**2
        h = float(input("Ingrese la altura del rectangulo: "))
        volumen = area * h
        print("El volumen de la piscina circular es: ",round(volumen,3),"cm3")

print("\tExamen Bimestral")
print("Bonilla Diana")
print("Carrillo Jessica")
print("Hernandez Edison")
print("Osorio Edison")
print("Sanchez Jordan")
print("Menu: \n")
print("1. Ejercicio 1")
print("\n2. Ejercicio 2")
print("\n3. Ejercicio 3")
opcion=int(input("Ingrese una opcion (Presione enter para salir): "))
if opcion == 1:
    ejercicio1()
elif opcion == 2:
    ejercicio2()
elif opcion == 3:
    ejercicio3()
else:
    print("Opcion Incorrecta..!!")
while opcion != "":
    os.system("clear")
    print("Menu: \n")
    print("1. Ejercicio 1")
    print("\n2. Ejercicio 2")
    print("\n3. Ejercicio 3")
    opcion=int(input("Ingrese una opcion (Presione enter para salir): "))
    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
        
    else:
        print("Opcion Incorrecta..!!")
    

    
        
    
