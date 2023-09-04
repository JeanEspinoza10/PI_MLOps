from app import api
from flask_restx import Resource
from flask import request
from app.controllers.genre_controller import Genre
from app.schemas.genre_schemas import GenreRequestSchema

# Documentación con la herramienta Swagger
genre_ns = api.namespace(
    name = "Genre",
    description = "",
    path = "/genre"
)

request_schema = GenreRequestSchema(genre_ns)



# Creando las rutas
@genre_ns.route("")
class User(Resource):
    @genre_ns.expect(request_schema.get())
    def get(self):
        controller = Genre()
        return controller.get(request.json)