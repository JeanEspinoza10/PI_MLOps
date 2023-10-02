import pandas as pd

from app.utils.db import ConnectionDB
def dataUsergenre():
    
    connection = ConnectionDB()

    db, client = connection.database('ProyectosoyHenry')

    
    coleccion_userForGenre_usuario = db['UserForGenre_usuario']

    # Consultar todos los documentos en la colección
    
    usuario = coleccion_userForGenre_usuario.find()

    # Convertir los resultados en una lista de diccionarios
    
    documentos_usuario = list(usuario)

    # Crear un DataFrame a partir de la lista de diccionarios
   
    df_usuario  = pd.DataFrame(documentos_usuario)

    return df_usuario


def dataAgrupadogenre():
    connection = ConnectionDB()

    db, client = connection.database('ProyectosoyHenry')

    
    coleccion_UserForGenre_items = db['UserForGenre_items']

    # Consultar todos los documentos en la colección
    
    items = coleccion_UserForGenre_items.find()

    
    # Convertir los resultados en una lista de diccionarios
    
    documentos_items = list(items)

    # Crear un DataFrame a partir de la lista de diccionarios
   
    df_items = pd.DataFrame(documentos_items)

    return df_items
