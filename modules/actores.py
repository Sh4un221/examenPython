import os
import json
from .variables import getAllActores,saveActores,actoresList

current_directory = os.path.dirname(os.path.abspath(__file__))
fileP = os.path.join(current_directory, '..', 'storage', 'peliculasData.json')

if os.path.exists(fileP) and os.path.getsize(fileP) > 0:
    with open(fileP, 'r') as file:
        actoresList.extend(json.load(file))
def crearActores():
    actor={
        "id"(input("Ingrese ID del actor: ")),
        "nombre"(input("Ingrese nombre del actor: "))
    }
    saveActores(actor)
