import modules.actores as ac
import modules.generos as ag
import modules.formatos as af
import modules.peliculas as ap
import os

def menuMaestro():
    menu=["Administrador de generos","Administrador de Actores","Administrador de Formatos","Gestor de informes","Gestor de peliculas","Salir"]
   
    while(True):
        os.system('cls')
        print("""
            ***************************************************
            ***** SISTEMA GESTOR DE PELICULAS BLOCKBUSTER *****
            ***************************************************
            """)
        print("".join([f"{i+1}.{val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1: ag.menuGeneros()
                    case 2: ac.menuActores()
                    case 3: af.menuFormatos()
                    case 4: ap.gestorDeInformes()
                    case 5: ap.menuPeliculas()
                    case 6: break
        except ValueError:
            print(f"La opcion es invalida, porfavor ingrese algo valido.")