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
                # Si la conversión es exitosa, retorna True
                
                # Filtrar el DataFrame para obtener los registros donde 'posted_year' sea igual a 2022
                registros_buscados = self.dataframe[self.dataframe['posted_year'] == entero].reset_index(drop=True)
                
                if not (registros_buscados.empty):


                    # Obtener los tres primeros registros con los mayores valores en la columna 'recommend'
                    primeros_tres_mayores = registros_buscados.nlargest(3, 'recommend').reset_index(drop=True)
                    
                    result = primeros_tres_mayores.to_dict('records')
                    
                
                    # JSON respuesta
                    data = []
                
                    for element in result:   
                        data.append(element["item_id"])
                    
                    
                    return {
                        "Result": 
                                {
                                    "Puesto 1" : f"Item_id: {data[0]}", 
                                    "Puesto 2" : f"Item_id: {data[1]}",
                                    "Puesto 3" : f"Item_id: {data[2]}",
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
                # Si la conversión es exitosa, retorna True
                
                # Filtrar el DataFrame para obtener los registros donde 'posted_year' sea igual a 2022
                registros_buscados = self.dataframe[self.dataframe['posted_year'] == entero].reset_index(drop=True)
                
                if not (registros_buscados.empty):


                    # Obtener los tres primeros registros con los mayores valores en la columna 'recommend'
                    primeros_tres_menores = registros_buscados.nsmallest(3, 'recommend').reset_index(drop=True)
                    
                    result = primeros_tres_menores.to_dict('records')
                    
                
                    # JSON respuesta
                    data = []
                
                    for element in result:   
                        data.append(element["item_id"])
                    
                    
                    return {
                        "Result": 
                                {
                                    "Puesto 1" : f"Item_id: {data[0]}", 
                                    "Puesto 2" : f"Item_id: {data[1]}",
                                    "Puesto 3" : f"Item_id: {data[2]}",
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

