import os
import json
from .variables import generosList

current_directory = os.path.dirname(os.path.abspath(__file__))
fileP = os.path.join(current_directory, '..', 'storage', 'generosData.json')

if os.path.exists(fileP) and os.path.getsize(fileP) > 0:
    with open(fileP, 'r') as file:
        generosList.extend(json.load(file))
def crearGenero():
    flag=True
    genero={
        "id":(input("Ingrese ID del genero: ")),
        "nombre":(input("Ingrese nombre del genero: "))
    }
    if(len(generosList)>0):
        for i,val in enumerate(generosList):
            if val['id']!=genero['id']:
                generosList.append(genero)
                break
            else:
                print("Este ID ya existe")
                break
    os.system('pause')
    with open(fileP, 'w') as file:
        json.dump(generosList, file, indent=2)
def leerGeneros():
    for i,val in enumerate(generosList):
        print(f"""
              Codigo: {i+1}
              ID: {val['id']}
              Nombre: {val['nombre']}
              """)
    os.system('pause')
        
def eliminarGenero():
    leerGeneros()
    ban=True
    while ban:
        print("Cual es el codigo del genero que desea eliminar")
        cod=int(input(""))
        actor=generosList.pop(cod-1)
        
        print(f"""
              Se elimino el genero:
              Nombre {actor['nombre']}
              """)
        with open(fileP, 'w') as file:
            json.dump(generosList, file, indent=2)
        os.system('pause')
        break
def menuActores():
    menu=["Crear genero","Listar genero","Eliminar genero"]
   
    while(True):
        os.system('cls')
        print("""
            *****************************
            ***** GESTOR DE GENEROS *****
            *****************************
            """)
        print("".join([f"{i+1}.{val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1: crearGenero()
                    case 2: leerGeneros()
                    case 3: eliminarGenero()
        except ValueError:
            print(f"La opcion es invalida, porfavor ingrese algo valido.")