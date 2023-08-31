import pymongo
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Accede a las variables de entorno cargadas
user = os.getenv("USER_DATA_BASE")
password = os.getenv("PASSWORD_DATA_BASE")

# Parseo para conectarme a la base de datos
mongo_uri = f"mongodb+srv://{user}:{password}@pruebas.r6rdxi9.mongodb.net/"

# Establece la conexión
client = pymongo.MongoClient(mongo_uri)

# Accede a una base de datos
db = client["ProyectosoyHenry"]

# Accede a una colección dentro de la base de datos
collection = db["users_reviews"]


# Realiza una consulta para encontrar documentos con user_id igual a "76561197970982479"
query = {"user_id": "76561197970982479"}
documentos = collection.find(query)


for documento in documentos:
    print(documento["reviews"][0])