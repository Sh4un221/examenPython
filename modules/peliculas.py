import os
import json
from .variables import peliculasList
import modules.actores as actor
import modules.formatos as formato
import modules.generos as genero

current_directory = os.path.dirname(os.path.abspath(__file__))
fileP = os.path.join(current_directory, '..', 'storage', 'peliculasData.json')

if os.path.exists(fileP) and os.path.getsize(fileP) > 0:
    with open(fileP, 'r') as file:
        peliculasList.extend(json.load(file))
        

def crearPelicula():
    flag=True
    pelicula={
        "id":(input("Ingrese ID de la pelicula: ")),
        "nombre":(input("Ingrese nombre de la pelicula: ")),
        "duracion":(input("Ingrese la duracion de la pelicula: ")),
        "sinopsis":(input("Ingrese la sinopsis: ")),
        "generos":[],
        "actores":[],
        "formato":[]
    }
    agregarGenero(pelicula)
    agregarActor(pelicula)
    agregarFormato(pelicula)
    if(len(peliculasList)>0):
        for i,val in enumerate(peliculasList):
            if val['id']!=pelicula['id']:
                peliculasList.append(pelicula)
                break
            else:
                print("Este ID ya existe")
                break
    else:
        peliculasList.append(pelicula)
    os.system('pause')
    with open(fileP, 'w') as file:
        json.dump(peliculasList, file, indent=2)
def leerPeliculas():
    for i,val in enumerate(peliculasList):
        print(f"""
              Codigo: {i+1}
              ID: {val['id']}
              Nombre: {val['nombre']}
              Duracion: {val['duracion']}
              """)
    os.system('pause')        
def eliminarPelicula():
    leerPeliculas()
    ban=True
    while ban:
        print("Cual es el codigo del genero que desea eliminar")
        cod=int(input(""))
        actor=peliculasList.pop(cod-1)
        
        print(f"""
              Se elimino el genero:
              Nombre {actor['nombre']}
              """)
        with open(fileP, 'w') as file:
            json.dump(peliculasList, file, indent=2)
        os.system('pause')
        break
def editarPelicula():
    leerPeliculas()
    ban=True
    while ban:
        print("Cual es el codigo del genero que desea editar")
        cod=int(input(""))
        print(peliculasList[cod-1])
        print("""
              Esta seguro que desea editarlo?: 
              1.Si
              2.No
              """)
        opt=int(input(""))
        if opt==1:
            peliculae={
            "id":(input("Ingrese ID de la pelicula: ")),
            "nombre":(input("Ingrese nombre de la pelicula: ")),
            "duracion":(input("Ingrese la duracion de la pelicula: ")),
            "sinopsis":(input("Ingrese la sinopsis: ")),
            "generos":[],
            "actores":[],
            "formato":[]                
            }
            agregarGenero(peliculae)
            agregarActor(peliculae)
            agregarFormato(peliculae)           
            peliculasList[cod-1]=peliculae
            with open(fileP, 'w') as file:
                json.dump(peliculasList, file, indent=2)
            print("Se modifico correctamente la pelicula")
            os.system('pause')
            break
        else:
            break  
def buscarPelicula():
    print("Ingrese el ID de la pelicula (Si no lo sabe puede mirar la lista de todas):")
    id=input("")
    for i,pelicula in enumerate(peliculasList):
        if(id==pelicula['id']):
            print(f"Nombre: {pelicula['nombre']}")
    os.system('pause')
    
        
def menuPeliculas():
    menu=["Crear una pelicula","Listar peliculas","Editar pelicula","Eliminar pelicula","Buscar pelicula","Salir"]
   
    while(True):
        os.system('cls')
        print("""
            ******************************
            ***** GESTOR DE PELICULAS *****
            ******************************
            """)
        print("".join([f"{i+1}.{val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1: crearPelicula()
                    case 2: leerPeliculas()
                    case 3: editarPelicula()
                    case 4: eliminarPelicula()
                    case 5: buscarPelicula()
                    case 6: break

        except ValueError:
            print(f"La opcion es invalida, porfavor ingrese algo valido.")
            
def agregarGenero(pelicula:dict):
    fl=True
    genero.leerGeneros()
    while fl:
        print("Ingrese el codigo del genero que desea agregar a la pelicula: ")
        codigo=int(input(""))
        pelicula['generos'].append(genero.generosList[codigo-1])
        print("""
              Desea seguir agregando mas generos?
              1. Si
              2. No
              """)
        opt=int(input())
        if opt!=1:
            fl=False
            break
def agregarActor(pelicula:dict):
    fl=True
    actor.leerActores()
    while fl:
        print("Ingrese el codigo del actor que desea agregar a la pelicula: ")
        codigo=int(input(""))
        pelicula['actores'].append(actor.actoresList[codigo-1])
        print("""
              Desea seguir agregando mas actores?
              1. Si
              2. No
              """)
        opt=int(input())
        if opt!=1:
            fl=False
            break
def agregarFormato(pelicula:dict):
    fl=True
    formato.leerFormatos()
    while fl:
        print("Ingrese el codigo del formato que tiene la pelicula: ")
        codigo=int(input(""))
        pelicula['formato'].append(formato.formatosList[codigo-1])
        print("""
              Desea seguir agregando mas formatos?
              1. Si
              2. No
              """)
        opt=int(input())
        if opt!=1:
            fl=False
            break
        
def gestorDeInformes():
    menu=["Listar peliculas de un genero especifico","Listar peliculas donde el protagonista sea Silvester Stallone","Buscar pelicula y mostrar la sinopsis y los actores","Ir al menu principal"]
    
    while(True):
        os.system('cls')
        print("""
            ******************************
            ***** GESTOR DE INFORMES *****
            ******************************
            """)
        print("".join([f"{i+1}.{val}\n" for i,val in enumerate(menu)]))
        try:
            opc=int(input())
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1: 
                        if len(peliculasList)>0:
                            genero.leerGeneros()
                            print("Ingrese el ID del genero por el cual desea buscar las peliculas: ")
                            genero1=input("")
                            for i,val in enumerate(peliculasList):
                                for generos in val['generos']:
                                    if(generos['id']==genero1):
                                        print(f"Pelicula {i+1}: {val['nombre']}") 
                                        
                            os.system('pause')
                        else:
                            print("No hay peliculas registradas")
                            os.system('pause')
                    case 2: 
                        if len(peliculasList)>0:
                            actor.leerActores()
                            print("Ingrese el ID del actor por el cual desea buscar las peliculas: ")
                            actor1=input("")
                            for i,val in enumerate(peliculasList):
                                for actores in val['actores']:
                                    if(actores['id']==actor1):
                                        print (f"Actores: {actores['nombre']}")
                                        print(f"Pelicula: {val['nombre']}")            
                            os.system('pause')
                        else:
                            print("No hay peliculas registradas")
                            os.system('pause')                        
                        
                    case 3: 
                        if len(peliculasList)>0:
                            leerPeliculas()
                            print("Cual es el ID de la pelicula que desea buscar")
                            cod=input()
                            for ind,val in enumerate(peliculasList):
                                if(val['id']==cod):
                                    print(f"Sinopsis {val['sinopsis']}")
                                    for autores in val['actores']:
                                        print(f"Actores: {autores['nombre']}")
                            os.system('pause')
                    
                    case 4: break
        except ValueError:
            print(f"La opcion es invalida, porfavor ingrese algo valido.")