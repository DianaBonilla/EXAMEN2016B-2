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
    archi=open('nombres.txt','r')
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
        a.write('Bonilla Valdivieso Diana Estefania \n')
        a.write('Carrillo Morocho Jessica Vanessa \n')
        a.write('Osorio Gonzalez Edison Santiago \n')
        a.write('Sanchez Hernandez Jordan Sebastian \n')
        a.write('Hernandez Alamgro Edison David \n')
        a.close()

    def leer():
        a=open('nombre.txt','r')
        linea=a.readline()
        while linea !='':
            print(linea)
            linea=a.readline()
        a.close()
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
    

    
        
    
