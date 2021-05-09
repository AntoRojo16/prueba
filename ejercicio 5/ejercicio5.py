from claseManejadorAlumno import Manejador
from ClaseMenuejercico5 import Menu
import os



if __name__=="__main__":
    
    unManejador=Manejador()
    unManejador.testAlumno()
    a=5
    d=4
    unManejador.listar(a,d)
    #unManejador.porcentajeIna(a,d)
    #unMenu=Menu()
    #print("MENU")
    #print("INGRESE LAOPCION 1 PARA EL ITEMA A \nINGRESE LA OPCION 2 PARA EL ITEM B ")
    #op=input()
    #unMenu.opcion(op,unManejador)
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2\n3. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op, unManejador)
        salir = op == 3
    print(salir)
    