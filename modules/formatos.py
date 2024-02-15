import os
import json
from .variables import formatosList

current_directory = os.path.dirname(os.path.abspath(__file__))
fileP = os.path.join(current_directory, '..', 'storage', 'formatosData.json')

if os.path.exists(fileP) and os.path.getsize(fileP) > 0:
    with open(fileP, 'r') as file:
        formatosList.extend(json.load(file))
def crearFormato():
    flag=True
    formato={
        "id":(input("Ingrese ID del formato: ")),
        "nombre":(input("Ingrese nombre del formato: "))
    }
    if(len(formatosList)>0):
        for i,val in enumerate(formatosList):
            if val['id']!=formato['id']:
                formatosList.append(formato)
                break
            else:
                print("Este ID ya existe")
                break
    else:
        formatosList.append(formato)
    os.system('pause')
    with open(fileP, 'w') as file:
        json.dump(formatosList, file, indent=2)
def leerFormatos():
    for i,val in enumerate(formatosList):
        print(f"""
              Codigo: {i+1}
              ID: {val['id']}
              Nombre: {val['nombre']}
              """)
    os.system('pause')
        
def eliminarFormato():
    leerFormatos()
    ban=True
    while ban:
        print("Cual es el codigo del formato que desea eliminar")
        cod=int(input(""))
        actor=formatosList.pop(cod-1)
        
        print(f"""
              Se elimino el formato:
              Nombre {actor['nombre']}
              """)
        with open(fileP, 'w') as file:
            json.dump(formatosList, file, indent=2)
        os.system('pause')
        break
def menuFormatos():
    menu=["Crear formato","Listar formato","Eliminar formato","Salir"]
   
    while(True):
        os.system('cls')
        print("""
            ******************************
            ***** GESTOR DE FORMATOS *****
            ******************************
            """)
        print("".join([f"{i+1}.{val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1: crearFormato()
                    case 2: leerFormatos()
                    case 3: eliminarFormato()
                    case 4: break
        except ValueError:
            print(f"La opcion es invalida, porfavor ingrese algo valido.")