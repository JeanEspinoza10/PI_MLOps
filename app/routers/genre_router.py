from app import api
from flask_restx import Resource
from flask import request
from app.controllers.genre_controller import Genre


# Documentación con la herramienta Swagger
genre_ns = api.namespace(
    name = "Genre",
    description = "",
    path = "/genre"
)





# Creando la ruta para el end point 
'''
def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
'''
@genre_ns.route("/PlayTimeGenre/<string:genero>")
class PlayTime(Resource):
    def get(self,genero):
        '''
        Debe devolver año con mas horas jugadas para dicho género.
        '''
        controller = Genre()
        return controller.playtime(genero)


'''
def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
'''
@genre_ns.route("/UserForGenre/<string:genero>")
class User(Resource):
    def get(self,genero):
        '''
        Debe devolver el usuario que acumula más horas jugadas para el género dado.
        '''
        controller = Genre()
        return controller.user(genero)
