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

def repetir():
    a=open('nombre.txt','w')
    for i in range (600):
        a.write('Bonilla Valdivieso Diana Estefania \n')
        a.write('Carrillo Morocho Jessica Vanessa \n')
        a.write('Osorio Gonzalez Edison Santiago \n')
        a.write('Sanchez Hernandez Jordan Sebastian \n')
        a.write('Hernandez Alamgro Edison David \n')

def main():
    crear()
    leer()
    repetir()

main()


