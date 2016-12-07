#ESCUELA POLITECNICA NACIONAL

from time import*
import os

def creartxt_ejercicio2():
    archi=open("Numero_Repeticiones.txt",'w')
    archi.close()

def leertxt_ejercicio2():
    tiempo=0
    repeticion=0
    nombre='Jordan'
    archi=open('****','r')
    inicio=time()
    linea=archi.readline()
    cadena=linea.split(' ')
    palabras=len(cadena-1)
    for i in range(palabras):
        if palabras[i]==nombre:
            repeticion=repeticion+1
    while linea != "":
        linea=archi.readline()
        cadena=linea.split(' ')
        palabras=len(palabras)
        for i in range(palabras):
            if palabras[i]==nombre:
                repeticion=repeticion+1
    fin=time()
    archi.close()
    tiempo=fin-inicio
    archi=open('Numero_Repeticiones.txt','a')
    archi.write('El numero de repeticiones es: ', str(repeticion))
    archi.write('\nEl tiempo transcurrido fue: ', str(tiempo))

def ejercicio1():
    ##Agregar Ejercicio 1...!!
    print("")

def ejercicio2():
    print("\tEjercicio 2")
    creartxt_ejercicio2()
    leertxt_ejercicio2()

def ejercicio3():
    ##Agregar ejercicio 3..!!
    print("")

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
else if opcion == 2:
    ejercicio2()
else if opcion == 3:
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
    else if opcion == 2:
        ejercicio2()
    else if opcion == 3:
        ejercicio3()
    else:
        print("Opcion Incorrecta..!!")
    

    
        
    
