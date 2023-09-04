from app import api
from flask_restx import Resource
from flask import request
from app.schemas.user_schemas import UserRequestSchema
from app.controllers.user_controller import UserController

# Documentación con la herramienta Swagger
user_data_ns = api.namespace(
    name = "User",
    description = "",
    path = "/user"
)

request_schema = UserRequestSchema(user_data_ns)



# Creando las rutas
@user_data_ns.route("data")
class User(Resource):
    @user_data_ns.expect(request_schema.get())
    def get(self):
        controller = UserController()
        return controller.get(request.json)


# Ruta para userforagenre

@user_data_ns.route("forgenre")
class User(Resource):
    @user_data_ns.expect(request_schema.userforgenre())
    def get(self):
        controller = UserController()
        return controller.get_userforgenre(request.json)