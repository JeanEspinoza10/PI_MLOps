
import pandas as pd
import numpy as np
import gc

class Prediccion:
    def __init__(self):
        self.top = 5
    def get(self, id):
        try:
            
            df_data = pd.read_json("app/prediccion/dataframe_nuevo.json")
            df_items = pd.read_json("app/prediccion/dataframe_items.json")
            prediccion = np.load('app/prediccion/users_predictions.npy')

            try:
                user_index = df_data[df_data['user_id'] == id].index[0]  # Obtén el índice del usuario en el DataFrame.
            
                if user_index:
                    # Ordena los índices de los ítems recomendados para el usuario en función de la puntuación de recomendación.
                    sorted_item_indices = prediccion[user_index].argsort()[::-1]

                    #Obtener los items
                    games=sorted_item_indices[:self.top].tolist()

                    # Variable donde almacenara la respuesta
                    
                    respuesta = []

                    for element in games:
                        items_id = df_data.loc[element]['item_id']
                        valor_buscar = int(items_id)
                    
                        if valor_buscar:

                            filas = df_items[df_items["id"] == valor_buscar]
                            # Obtener el valor de 'app_name' de las filas filtradas
                            app_name = filas['app_name'].tolist()
                            
                            
                            respuesta.append(app_name[0])

                    # Forzar la recolección de basura para liberar memoria
                    gc.collect()
                    return {
                        "Result": {
                        
                            f"Te recomendamos los siguientes juegos": respuesta
                            
                            },
                        "Code": 200
                    },200


                else:           
                    return {
                        "Result":f"Usuario id: {id} no se encontro.",
                        "Code": 404
                    },404


            except Exception as e:
                print(e)
                return {
                    "Result": f"{e}",
                    "Code": 400
                }, 400
            
            

        except Exception as e:
            print(e)

            return {
                "Result":f"{e}",
                "Code":500
            },500

            