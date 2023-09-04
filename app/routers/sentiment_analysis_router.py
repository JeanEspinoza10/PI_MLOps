from app import api
from flask_restx import Resource
from flask import request
from app.schemas.sentiment_schema import SentimentAnalysisRequestSchema
from app.controllers.sentiment_analysis_controller import Sentiment

# Documentación con la herramienta Swagger
sentiment_analysis_ns = api.namespace(
    name = "Sentiment Analysis",
    description = "",
    path = "/sentiment_analysis"
)

request_schema = SentimentAnalysisRequestSchema(sentiment_analysis_ns)

# Creando las rutas
@sentiment_analysis_ns.route("")
class User(Resource):
    @sentiment_analysis_ns.expect(request_schema.count())
    def get(self):
        controller = Sentiment()
        return controller.count(request.json)

