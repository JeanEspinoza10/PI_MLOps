import re
from flask import jsonify
from app.utils.users_reviews import UsersReviews
from datetime import datetime, time
from app.helpers.fechas import convertir_fecha
class Reviews:
    def __init__(self):
        self.userreviews = UsersReviews()
    def count(self,fecha_inicio, fecha_fin):
        try:
            # Define una expresión regular para el formato "YYYY-MM-DD"
            patron = r"^\d{4}-\d{2}-\d{2}$"
            # Comprueba si la fecha coincide con el patrón
            if re.match(patron, fecha_inicio) and re.match(patron, fecha_fin):
                
                # Convierte las fechas en objetos datetime
                fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
                
                 # Verifica si fecha_inicio es menor que fecha_fin
                if fecha_inicio_dt < fecha_fin_dt:
                    # Inicializamos los contadores
                    count_reviews = 0
                    recomend = []
                    # Obtenemos los documentos de nuestra base de datos
                    documents , client = self.userreviews.BuscarAll()
                    
                    # Iteramos sobre cada documento
                    if documents:
                        for element in documents:
                            reviews = element["reviews"]
                            if reviews:
                                for review in reviews:
                                    try:            
                                        posted = datetime.combine(convertir_fecha(review["posted"]),time(00, 00, 00))
                                        if fecha_inicio_dt <= posted <= fecha_fin_dt:
                                            count_reviews += 1
                                            recomend.append(review["recommend"])
                                    except Exception as e:
                                        print(e)
                                        continue
                                


                        if recomend:
                            # Calcula el porcentaje de True
                            recomend_porcentaje = (recomend.count(True) / len(recomend)) * 100
                        else:
                            recomend_porcentaje = 0
                        result = {
                                "Cantidad de usuarios-reviews": count_reviews,
                                "Porcentaje de Recomendado": recomend_porcentaje
                            }

                        
                        return result, 200


                    else:
                        return {
                        "error": f"Result: Sin documentos en nuestra base de datos"
                        },200
                                           
                else:
                    return {
                    "error": f"Error en reviewscounts: Colocar la fecha_inicio < fecha_fin"
                    },400

            else:
                return {
                "error": f"Error en reviewscounts: Colocar las fechas en el formato YYYY-MM-DD"
            },400
             


        except Exception as e:
            return {
                "error": f"Error en reviewscounts: {e}"
            }, 400