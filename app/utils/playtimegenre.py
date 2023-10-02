import pandas as pd
from app.utils.db import ConnectionDB

def dataPlaytime():
    
    connection = ConnectionDB()

    db, client = connection.database('ProyectosoyHenry')

    coleccion = db['playtimegenre']


    # Consultar todos los documentos en la colección
    resultados = coleccion.find()


    # Convertir los resultados en una lista de diccionarios
    documentos = list(resultados)


    # Crear un DataFrame a partir de la lista de diccionarios
    df = pd.DataFrame(documentos)

    return df
    







