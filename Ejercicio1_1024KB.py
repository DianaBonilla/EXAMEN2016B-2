def texto():
    archi=open('nombres.txt','w')
    archi=open('nombres.txt','a')
    archi.write('Bonilla Valdivieso Diana Estefania\n')
    archi.write('Carrillo Morocho Jessica Vanessa\n')
    archi.write('Hernandez Almagro Edison David\n')
    archi.write('Osorio Gonzales Edison Santiago\n')
    archi.write('Sanchez Hernandez Jordan Sebastian\n')
    archi.close()
   



def repetir():
    archi=open('nombres.txt','w')
    for i in range(6189):
        archi.write('Bonilla Valdivieso Diana Estefania\n')
        archi.write('Carrillo Morocho Jessica Vanessa\n')
        archi.write('Hernandez Almagro Edison David\n')
        archi.write('Osorio Gonzales Edison Santiago\n')
        archi.write('Sanchez Hernandez Jordan Sebastian\n')
    archi.close()


def leer():
    archi=open('nombres.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        linea=archi.readline()
    archi.close()
        


texto()
repetir()
leer()

  

    
    
