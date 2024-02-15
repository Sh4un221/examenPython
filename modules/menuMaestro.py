import modules.actores as ac
import os

def menuMaestro():
    menu=["Administrador de generos","Administrador de Actores","Administrador de Formatos","Gestor de informes","Gestor de peliculas","Salir"]
   
    while(True):
        os.system('cls')
        print("""
            ******************
            ***** TITULO *****
            ******************
            """)
        print("".join([f"{i+1}.{val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1: pass
                    case 2: ac.menuActores()
                    case 3: pass
                    case 4: pass
                    case 5: pass
                    case 6: pass
        except ValueError:
            print(f"La opcion es invalida, porfavor ingrese algo valido.")