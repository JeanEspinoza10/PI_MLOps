from app import api
from flask_restx import Resource
from flask import request
from app.controllers.reviews_controller import Reviews
from app.schemas.reviews_schemas import ReviewsRequestSchema

# Documentación con la herramienta Swagger
reviews_ns = api.namespace(
    name = "Count Reviews",
    description = "",
    path = "/countreviews"
)

request_schema = ReviewsRequestSchema(reviews_ns)



# Creando las rutas
@reviews_ns.route("/<string:fecha_inicio>/<string:fecha_fin>")
class User(Resource):
    def get(self,fecha_inicio,fecha_fin):
        controller = Reviews()
        return controller.count(fecha_inicio,fecha_fin)