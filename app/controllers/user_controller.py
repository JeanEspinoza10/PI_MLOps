import os
from flask import jsonify
from app.utils.users_items import UsersItems
from app.utils.steam_games import SteamGames
from app.utils.users_reviews import UsersReviews

class UserController:
    def __init__(self):
        self.usersItems = UsersItems()
        self.steamsgames = SteamGames()
        self.userreviews = UsersReviews()
    def get(self,id):
        try:
            # Obtenemos el documento en formato de diccionario
            documents, client = self.usersItems.BuscarID(id)

            if documents:
                documents = documents[0]            
                # Obteniendo los valores necesarios para realizar la respuesta.
                price = []
                recomend = []
                count_items =documents["items_count"]
                
                # Obteniendo el precio de cada juego
                juegos = documents["items"]
                for element in juegos:
                    item_id = element["item_id"]
                    detail, client = self.steamsgames.BuscarID(item_id)
                    if detail:
                        price.append(detail[0]["price"])
                
                # Utiliza una comprensión de lista para sumar solo los valores numéricos
                suma = sum(item for item in price if isinstance(item, (int, float)))
                
                # Obtenemos de la coleccion users_review las recomendaciones del usuario id
                reviews, client = self.userreviews.BuscarID(id)
                if reviews:
                    all_reviews = reviews[0]["reviews"]
                    for element in all_reviews:
                        recomend.append(element["recommend"])
                
                # Calcula el porcentaje de True
                porcentaje_true = (recomend.count(True) / len(recomend)) * 100
                
                result = {
                    "Total Gastado": suma,
                    "Total de items": count_items,
                    "Porcentaje de Recomendado": porcentaje_true
                }
                
            else:
                result = {
                    "result": "No hay items relacionados con el usuario_id en nuestra base de datos."
                }

            client.close()

            return  result
        except Exception as e:
            return {
                "error": f"Error en user_controller: {e}"
            }
    def get_userforgenre(data):
        try:
            pass
        except Exception as e:
            pass