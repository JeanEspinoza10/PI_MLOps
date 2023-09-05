from app.utils.db import ConnectionDB



class UsersItems:
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
            collection = database["users_items"]

            # Variable id a buscar
            query = {"user_id": id}


            # Realizar la busqueda en la coleccion y obtener el documento.
            documents = list(collection.find(query))
            
            return documents,client
        except Exception as e:
            raise Exception("Error en la clase UsersItems:" + str(e))         




