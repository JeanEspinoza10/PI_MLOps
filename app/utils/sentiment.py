import pandas as pd
from app.utils.db import ConnectionDB

def dataSentiment():
    
    connection = ConnectionDB()
    
    db, client = connection.database('ProyectosoyHenry')

    
    coleccion_recommendUser = db['Sentiment_analysis']

    # Consultar todos los documentos en la colección
    
    recommend = coleccion_recommendUser.find()

    

    # Convertir los resultados en una lista de diccionarios
    
    documentos_recommend = list(recommend)

    # Crear un DataFrame a partir de la lista de diccionarios
   
    df_sentiment = pd.DataFrame(documentos_recommend)

    return df_sentiment



