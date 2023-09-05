from app.utils.db import ConnectionDB

class UsersReviews:
    def __init__(self):
        self.connection = ConnectionDB()

    def BuscarID(self,id):
        """
        Busca un documento en la colección users_items por el ID de usuario.

        Args:
            id (str): El ID de usuario a buscar.

        Returns:
            list: Una lista de documentos que coinciden con el ID de usuario.
        """
        try:
            # Conexion a la base de datos
            database, client = self.connection.database("ProyectosoyHenry")
            collection = database["users_review"]

            # Variable id a buscar
            query = {"user_id": id}


            # Realizar la busqueda en la coleccion y obtener el documento.
            documents = list(collection.find(query))

          
            return documents, client
        except Exception as e:
            raise Exception("Error en la clase UsersReviews:" + str(e))    

    def BuscarAll(self):
        try:
            # Conexion a la base de datos
            database, client = self.connection.database("ProyectosoyHenry")
            collection = database["users_review"]


            # Realizar la busqueda en la coleccion y obtener el documento.
            documents = list(collection.find())

          
            return documents, client
        except Exception as e:
            raise Exception("Error en la clase UsersReviews:" + str(e))