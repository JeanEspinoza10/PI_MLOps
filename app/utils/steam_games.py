from app.utils.db import ConnectionDB

class SteamGames:
    def __init__(self):
        self.connection = ConnectionDB()

    def BuscarID(self,id):
        """
        Se conecta a la coleccion steam_games de la base de datos Proyectosoyhenry,
        obteniendo el documento por el id
        Args:
            id: identificador del documento
        Returns:
            list: la lista de documentos para esta busqueda realizada.
        """
        try:
            # Realizando la conexion a la base de datos
            database, client = self.connection.database("ProyectosoyHenry")
            collection = database["steam_games"]
            # Buscando al documento
            query = {"id": id}
            documents = list(collection.find(query))
            
            
            return documents,client
        except Exception as e:
            raise Exception("Error en clase SteamGames-BuscarID:" + str(e))  
    



