formatosList=list()
generosList=list()
peliculasList=list()
actoresList=list()

def saveFormatos(data):
    formatosList.append(data)
def savePeliculas(data):
    generosList.append(data)
def saveGeneros(data):
    peliculasList.append(data)
def saveActores(data):
    actoresList.append(data)

def getAllFormatos():
    return formatosList
def getAllPeliculas():
    return peliculasList
def getAllGeneros():
    return generosList
def getAllActores():
    return generosList


