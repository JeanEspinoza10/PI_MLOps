from app.utils.db import ConnectionDB
import time



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
            # Registra el tiempo de inicio
            inicio = time.time()
            # Conexion a la base de datos
            database, client = self.connection.database("ProyectosoyHenry")
            collection = database["users_items"]

            # Variable id a buscar
            query = {"user_id": id}


            # Realizar la busqueda en la coleccion y obtener el documento.
            documents = list(collection.find(query))
                        
            # Registra el tiempo de finalización
            fin = time.time()
            # Calcula el tiempo transcurrido
            tiempo_transcurrido = fin - inicio

            print(f"La consulta o código tomó {tiempo_transcurrido} segundos.")
            return documents,client
        except Exception as e:
            raise Exception("Error en la clase UsersItems:" + str(e))         




