from app import api
from flask_restx import Resource
from flask import request
from app.controllers.sentiment_controller import SentimentAnalysis
# Documentacion Swagger

sentiment_ns = api.namespace(
    name = "Sentiment",
    description = "",
    path = "/sentiment"
)

# Creando la ruta del endpoint
@sentiment_ns.route("/sentiment_analysis/<string:anio>")
class Sentiment(Resource):
    def get(self, anio):
        '''
        Algoritmo de sentimiento de Análisis
        '''
        controller = SentimentAnalysis()
        return controller.analysis(anio)
        
