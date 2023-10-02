import gc
from app.utils.playtimegenre import dataPlaytime
from app.utils.userforgenre import dataUsergenre, dataAgrupadogenre


class Genre:
    def __init__(self):
        
        self.usuario = 'usuario'

    def playtime(self,genero):
        '''
        imput: Genero es un string
        return: Json  {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
        '''
        try:
            # Obteniendo el dataframe correspondiente para el end point
            
            df = dataPlaytime()
           
            
            # Normalizando el dato de genero
            lower_genre = genero.lower()
            
            
            # Buscar filas en la columna donde genres = lower_genre
            filas_con_action = df[df['genres'].str.contains(lower_genre)]


            if not filas_con_action.empty:

                # Agrupar por 'release_year' y sumar 'playtime_forever' para cada grupo
                resultados_agrupados = filas_con_action.groupby('release_year')['playtime_forever'].sum()

                # Reindexar el resultado y ordenarlo de mayor a menor
                resultados_agrupados = resultados_agrupados.reset_index().sort_values(by='playtime_forever', ascending=False)

                # Obtener el primer registro del DataFrame ordenado
                time_registro = resultados_agrupados.iloc[0]

                # Convertir la Serie a una lista
                respuesta = time_registro.tolist()
                
                # Forzar la recolección de basura para liberar memoria
                gc.collect()
                
                # La respuesta esta: [fecha , time play forever]
                return {
                    'Result': f'Año de lanzamiento con más horas jugadas para Género {genero} es: {respuesta[0]} con {respuesta[1]} horas',
                    'Code': 200
                },200

            else:
                return {
                    'Result': 'No se encontro el Género en nuestra base de datos',
                    'Code': 404
                }, 404

            
        except Exception as e:
            print(e)
            return {
                'Result':f'{e}',
                'Code':500
            },500


    def user(self,genero):
        '''
        imput: Genero es un string
        return: Json  {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
        '''
        try:
            df_usuario = dataUsergenre()
            df_agrupado = dataAgrupadogenre()

            if not (df_agrupado.empty and df_usuario.empty):
                valor_genres = genero.lower()

                # Filtrar el DataFrame para encontrar las filas que contienen el valor buscado en 'genres'
                resultados = df_usuario[df_usuario['genres'] == valor_genres]

                # Encontrar el índice del máximo valor en 'playtime_forever'
                indice_maximo = resultados['playtime_forever'].idxmax()

                # Obtener el registro con el máximo valor de 'playtime_forever'
                registro_maximo = (resultados.loc[indice_maximo].tolist())[2]
                
                # Filtrar el DataFrame para encontrar las filas que contienen el valor buscado en 'user_id'
                resultado_respuesta = df_agrupado[df_agrupado['user_id'] == registro_maximo]

                # Filtrar el DataFrame para encontrar las filas que contienen el valor buscado en 'genres'
                result_finsh = (resultado_respuesta[resultado_respuesta['genres']== valor_genres]).reset_index(drop=True)

                
                # Eliminar las filas donde 'playtime_forever' sea igual a 0
                resultados_filtrados = result_finsh.query('playtime_forever != 0')
               

                # Convertir a una lista
                respuesta = resultados_filtrados.to_dict('records')
                
                # JSON
                json_respuesta = {}
                data_respuesta = []
                for element in respuesta:
                    json_respuesta["Año"] = element["release_year"]
                    json_respuesta["Horas"] = element["playtime_forever"]
                    data_respuesta.append(json_respuesta)

                # Forzar la recolección de basura para liberar memoria
                gc.collect()
                return {
                    'Result': {
                        f"Usuario con más horas jugadas para Género {respuesta[0]['genres']}": respuesta[0]["user_id"],
                        "Horas jugadas": data_respuesta
                    }
                },200
            
            else:
                return{
                    'Result': 'No se encontro registro en la base de datos'
                },400

        except Exception as e:
            print(e)
            return {
                'Result':f'{e}',
                'Code':500
            },500