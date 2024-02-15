import os
import json
from .variables import getAllActores,saveActores,actoresList

current_directory = os.path.dirname(os.path.abspath(__file__))
fileP = os.path.join(current_directory, '..', 'storage', 'peliculasData.json')
