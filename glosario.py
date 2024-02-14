# current_directory = os.path.dirname(os.path.abspath(__file__))#Parcear la ruta a la del computador que esta ejecutando el codigo

# fileP = os.path.join(current_directory, '..', 'storage', 'productsData.json')#Se especifica el lugar en donde el programa debe buscar el archivo json

# if os.path.exists(fileP) and os.path.getsize(fileP) > 0:#Comprobacion para que si el archivo json esta vacio no rompa el sistema

#     with open(fileP, 'r') as file:#Comando de libreria python para leer la informacion y traerla al sistema
#         productList.extend(json.load(file))
#Nota con la escritura. Como se usa listas en variables.py entonces asegurarse de usar la funcion de save antes de escribir porque de lo contrario se rompera el programa
#     with open(fileP, 'w') as file:#Comando de json en python para escribir la informacion en nuestro archivo json
#          json.dump(productList, file, indent=2)

# def menuProducts():
#     menu=[Opciones]
#    
#     while(True):
#         os.system('cls')
#         print("""
#             ******************
#             ***** TITULO *****
#             ******************
#             """)
#         print("".join([f"{i+1}.{val}\n" for i,val in enumerate(menu)]))=Ternario encargado de construir e imprimir el menu
#         try:
#             opc=int(input())
#             if(opc<=len(menu) and opc>0):
#                 match(opc):
#                     case 1: Funcion1
#                     case 2: .....
#         except ValueError:
#             print(f"La opcion es invalida, porfavor ingrese algo valido.")