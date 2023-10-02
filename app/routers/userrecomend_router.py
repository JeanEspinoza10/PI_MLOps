from app import api
from flask_restx import Resource
from flask import request
from app.controllers.userrecomend_controller import Prediccion

# Documentacion de Swagger

userrecomend_ns = api.namespace(
    name = "Algoritmo de Recomendación",
    description = "",
    path = "/recomend"
)

# Creando la ruta
@userrecomend_ns.route("/recomendacion_usuario/<string:id_usuario>")
class UserRecomend(Resource):
    def get(self,id_usuario):
        '''
        End point para consultar el algoritmo de prediccion
        '''
        controller = Prediccion()
        return controller.get(id_usuario)