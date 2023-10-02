from app import api
from flask_restx import Resource
from flask import request
from app.controllers.recommed_controller import Recommend
from app.schemas.recommend_schemas import RecommendRequestSchema

# Documentación con la herramienta Swagger
recommend_ns = api.namespace(
    name = "Recommend",
    description = "",
    path = "/recommend"
)

request_schema = RecommendRequestSchema(recommend_ns)

# Crenado la ruta para los endpoint
'''
def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
'''
@recommend_ns.route("/UsersRecommend/<string:anio>")
class RecommendTop(Resource):
    def get(self,anio):
        '''
        Devuelve el top 3 de juegos MÁS recomendados
        '''
        controller = Recommend()
        return controller.topRecomen(anio)


'''
def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

'''
@recommend_ns.route("/UsersNotRecommend/<string:anio>")
class RecommendDown(Resource):
    def get(self,anio):
        '''
        Devuelve el top 3 de juegos MENOS recomendados
        '''
        controller = Recommend()
        return controller.dowRecomen(anio)