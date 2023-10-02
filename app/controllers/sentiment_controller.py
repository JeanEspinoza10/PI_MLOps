import gc
from app.utils.sentiment import dataSentiment

class SentimentAnalysis:
    def __init__(self):
        self.dataframe = dataSentiment()

    def analysis(self, anio):
        
        try:
            df = self.dataframe
            try:
                # Cambiar el valor a un entero, en caso no se pueda arrojara un error como respuesta.
                valor_buscar = int(anio)

                
                # Filtrar el DataFrame para obtener los registros donde 'posted_year' sea igual a 2022
                registros_buscados = df[df['posted_year'] == valor_buscar].reset_index(drop=True)
                
                
                if not registros_buscados.empty:
                    # Agrupar por 'sentiment_analysis' y sumar 'num_sentiment_analysis'
                    result_sentiment = registros_buscados.groupby('sentiment_analysis')['num_sentiment_analysis'].value_counts()

                    # Crear un diccionario con el formato deseado
                    sentiment_dict = {
                        'Negative': result_sentiment.get(('neg', 0), 0),
                        'Neutral': result_sentiment.get(('neu', 1), 0),
                        'Positive': result_sentiment.get(('pos', 2), 0)
                    }

                    # Forzar la recolección de basura para liberar memoria
                    gc.collect()
                    return {
                        "Result": f"{sentiment_dict}",
                        "Code": 200
                    },200
                
                else:
                    return {
                        'Result': 'No se encontro el año en nuestra base de datos',
                        'Code': 404
                    }, 404

            except Exception as e:
                print(e) 
                return {
                    "Result": f"{e}",
                    "Code":400
                },400


            
            
        except Exception as e :
            print(e)
            return {
                "Result": f"{e}",
                "Code": 500
            },500
        

