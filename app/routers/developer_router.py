from app import api
from flask_restx import Resource
from flask import request
from app.schemas.developer_schemas import DeveloperRequestSchema
from app.controllers.developer_controller import Developer
# Documentación con la herramienta Swagger
developer_ns = api.namespace(
    name = "Developer",
    description = "",
    path = "/developer"
)
request_schema = DeveloperRequestSchema(developer_ns)

# Creando las rutas
@developer_ns.route("")
class User(Resource):
    @developer_ns.expect(request_schema.get())
    def get(self):
        controller = Developer()
        return controller.get(request.json)