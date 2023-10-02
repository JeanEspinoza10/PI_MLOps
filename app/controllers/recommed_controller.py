import gc
import pandas as pd
from app.utils.recommenduser import dataRecommend


class Recommend:
    def __init__(self):
        self.dataframe = dataRecommend()

    def topRecomen(self,anio):
        '''
        Valor: Año
        retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
        '''
        try:
            try:
                 # Intenta convertir la cadena a un entero
                entero = int(anio)
                # Obtener
                df_items = pd.read_json("app/prediccion/dataframe_items.json")

                # Filtrar el DataFrame para obtener los registros donde 'posted_year' sea igual a 2022
                registros_buscados = self.dataframe[self.dataframe['posted_year'] == entero].reset_index(drop=True)
                
                if not (registros_buscados.empty):


                    # Obtener los tres primeros registros con los mayores valores en la columna 'recommend'
                    primeros_tres_mayores = registros_buscados.nlargest(3, 'recommend').reset_index(drop=True)
                    
                    result = primeros_tres_mayores.to_dict('records')
                    
                
                    # JSON respuesta
                    data = []
                    respuesta = []
                    for element in result:   
                        data.append(element["item_id"])
                    
                    # Utilizar loc para buscar por 'id' y obtener 'app_name'
                    resultado = df_items.loc[df_items['id'] == int(data[1]), 'app_name'].to_dict()
                    
                    for element in data:
                        resultado = df_items.loc[df_items['id'] == int(element), 'app_name'].to_dict()
                        if resultado:
                            for key, value in resultado.items():
                                respuesta.append(value)
                        else:
                            respuesta.append(element)


                    # Forzar la recolección de basura para liberar memoria
                    gc.collect()
                    return {
                        "Result": 
                                {
                                    "Puesto 1" : f"Item: {respuesta[0]}", 
                                    "Puesto 2" : f"Item: {respuesta[1]}",
                                    "Puesto 3" : f"Item: {respuesta[2]}",
                                },
                        "Code": 200                    
                        }, 200
                
                else:
                    return {
                    "Result": f"Año no fue encontrado",
                    "Code":404
                    },400

                
            except ValueError as e:
                print(e)
                return {
                    "Result": f"{e}",
                    "Code":400
                },400

        except Exception as e:
            print(e)
            return {
                "Result":f"{e}",
                "Code":500
            },500


    def dowRecomen(self,anio):
        '''
        Valor: Año
        retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
        '''
        try:
            try:
                 # Intenta convertir la cadena a un entero
                entero = int(anio)
                

                df_items = pd.read_json("app/prediccion/dataframe_items.json")
                

                # Filtrar el DataFrame para obtener los registros donde 'posted_year' sea igual a 2022
                registros_buscados = self.dataframe[self.dataframe['posted_year'] == entero].reset_index(drop=True)
                
                if not (registros_buscados.empty):


                    # Obtener los tres primeros registros con los mayores valores en la columna 'recommend'
                    primeros_tres_menores = registros_buscados.nsmallest(3, 'recommend').reset_index(drop=True)
                    
                    result = primeros_tres_menores.to_dict('records')
                    
                
                    # JSON respuesta
                    data = []
                    respuesta = []
                    for element in result:
                        data.append(element["item_id"])
                    
                    # Utilizar loc para buscar por 'id' y obtener 'app_name'
                    resultado = df_items.loc[df_items['id'] == int(data[1]), 'app_name'].to_dict()
                    
                    for element in data:
                        resultado = df_items.loc[df_items['id'] == int(element), 'app_name'].to_dict()
                        if resultado:
                            for key, value in resultado.items():
                                respuesta.append(value)
                        else:
                            respuesta.append(element)


                    # Forzar la recolección de basura para liberar memoria
                    gc.collect()
                    return {
                        "Result": 
                                {
                                    "Puesto 1" : f"Item: {respuesta[0]}", 
                                    "Puesto 2" : f"Item: {respuesta[1]}",
                                    "Puesto 3" : f"Item: {respuesta[2]}",
                                },
                        "Code": 200                    
                        }, 200
                
                else:
                    return {
                    "Result": f"Año no fue encontrado",
                    "Code":404
                    },404

                
            except ValueError as e:
                print(ValueError)
                return {
                    "Result": f"{e}",
                    "Code":400
                },400

        except Exception as e:
            print(e)
            return {
                "Result":f"{e}",
                "Code":500
            },500

