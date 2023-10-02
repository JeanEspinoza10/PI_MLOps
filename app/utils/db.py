import pymongo
import os
from dotenv import load_dotenv

class ConnectionDB:
    def __init__(self):
        # Carga las variables de entorno desde el archivo .env
        load_dotenv()

        # Accede a las variables de entorno cargadas
        self.user = os.getenv("USER_DATA_BASE")
        self.password = os.getenv("PASSWORD_DATA_BASE")

        # Parseo para conectarme a la base de datos
        mongo_uri = f"mongodb+srv://{self.user}:{self.password}@pruebas.r6rdxi9.mongodb.net/"

        # Establece la conexión utilizando un bloque "with" para garantizar el cierre adecuado
        self.client = pymongo.MongoClient(mongo_uri)

    def database(self,name):
        """
        Se conecta a la base de base de datos
        Args:
            name: nombre de la base de datos
        
        Returns:
            list: el objeto de conexion a la base de datos
        """
        db = self.client[name]
        return db, self.client